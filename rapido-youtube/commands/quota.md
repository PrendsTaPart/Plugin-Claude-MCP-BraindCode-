---
description: Le quota du jour - consommé, réservé sous 24 h, disponible réel, risque, et ce qui tient encore
---

Lit yt_get_quota_status et restitue les quatre nombres (quota du jour,
consommé, réservé aux publications sous 24 h, disponible réel) + le
risque. Sur demande d'une campagne : python3
${CLAUDE_PLUGIN_ROOT}/scripts/quota.py dit si elle tient — will_fail =
revue du planning d'abord (yt_list_schedule).
