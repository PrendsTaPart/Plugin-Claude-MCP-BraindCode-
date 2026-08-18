import assert from "node:assert/strict";
import test from "node:test";

import {
  classifyToolCall,
  containsSensitiveInput,
  mustBlockRequester,
  parseMcpToolName,
} from "../policy.js";

test("parses the OpenClaw bundle-mcp tool naming convention", () => {
  assert.deepEqual(parseMcpToolName("rapidocms__list_brands"), {
    server: "rapidocms",
    tool: "list_brands",
  });
  assert.deepEqual(parseMcpToolName("mcp__rapidocms__list_brands"), {
    server: "rapidocms",
    tool: "list_brands",
  });
  assert.equal(parseMcpToolName("list_brands"), null);
});

test("allows recognized reads on protected Rapido servers", () => {
  assert.equal(classifyToolCall("rapidocms__list_brands", {}).action, "allow");
  assert.equal(classifyToolCall("rapidocrm__get_contact", { id: "42" }).action, "allow");
});

test("requires one-time approval for writes", () => {
  const warning = classifyToolCall("rapidorh__update_project", { id: "42" });
  assert.equal(warning.action, "approve");
  assert.equal(warning.severity, "warning");

  const critical = classifyToolCall("rapidocms__publish_post", { id: "42" });
  assert.equal(critical.action, "approve");
  assert.equal(critical.severity, "critical");

  const nounFirst = classifyToolCall("rapidocms__post_publish_now", { id: "42" });
  assert.equal(nounFirst.severity, "critical");
});

test("requires approval even for read-like calls on paid services", () => {
  const decision = classifyToolCall("dataforseo__search_keywords", { query: "test" });
  assert.equal(decision.action, "approve");
  assert.equal(decision.severity, "critical");
  assert.equal(decision.reason, "paid_service");
});

test("fails closed for unknown protected tools", () => {
  const decision = classifyToolCall("foodeatup__reconcile_magic", {});
  assert.equal(decision.action, "approve");
  assert.equal(decision.reason, "unknown_tool");
});

test("does not interfere with unrelated OpenClaw tools", () => {
  assert.equal(classifyToolCall("weather", {}).action, "ignore");
  assert.equal(classifyToolCall("github__get_issue", {}).action, "ignore");
});

test("blocks a proven non-owner and preserves local operator runs", () => {
  assert.equal(mustBlockRequester({ senderIsOwner: false }), true);
  assert.equal(mustBlockRequester({}), true);
  assert.equal(mustBlockRequester({ senderIsOwner: true }), false);
  assert.equal(mustBlockRequester(undefined), false);
});

test("detects nested secret-like input without logging the value", () => {
  assert.equal(containsSensitiveInput({ nested: { api_key: "do-not-log" } }), true);
  assert.equal(containsSensitiveInput({ campaign: { id: "123" } }), false);
  const decision = classifyToolCall("rapidocrm__get_contact", {
    headers: { authorization: "do-not-log" },
  });
  assert.equal(decision.action, "block");
  assert.equal(decision.severity, "critical");
  assert.equal(decision.reason, "sensitive_input");
});
