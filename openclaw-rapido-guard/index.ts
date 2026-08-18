import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";

import { classifyToolCall, mustBlockRequester } from "./policy.js";

const APPROVAL_TIMEOUT_MS = 120_000;

export default definePluginEntry({
  id: "rapido-guard",
  name: "Rapido Guard",
  description: "Approval gate for write, destructive, paid and unknown Rapido MCP calls.",
  register(api) {
    api.on("before_tool_call", async (event, ctx) => {
      const toolName = event?.toolName ?? "";
      const input = event?.params ?? event?.input ?? event?.arguments ?? {};
      const decision = classifyToolCall(toolName, input);

      if (decision.action === "ignore") {
        return undefined;
      }
      if (mustBlockRequester(ctx?.requester)) {
        api.logger?.warn?.("[rapido-guard] blocked MCP call from a non-owner requester");
        return {
          block: true,
          blockReason: "Rapido MCP tools require the verified channel owner.",
        };
      }
      if (decision.action === "allow") return undefined;
      if (decision.action === "block") {
        api.logger?.warn?.("[rapido-guard] blocked MCP input containing a secret-like field");
        return {
          block: true,
          blockReason: "Secret-like values must be configured outside MCP tool parameters.",
        };
      }

      api.logger?.warn?.(
        `[rapido-guard] approval required: ${decision.server}__${decision.tool} (${decision.reason})`,
      );

      return {
        requireApproval: {
          title: `Valider l'action Rapido : ${decision.tool}`,
          description:
            `Le serveur ${decision.server} demande une action non strictement en lecture ` +
            `(${decision.reason}). Vérifiez la cible et l'impact avant d'autoriser une seule fois.`,
          severity: decision.severity,
          allowedDecisions: ["allow-once", "deny"],
          timeoutMs: APPROVAL_TIMEOUT_MS,
        },
      };
    }, { priority: 100 });
  },
});
