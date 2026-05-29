<img width="143" height="150" alt="secure_ai_gateway_architecture_1" src="https://github.com/user-attachments/assets/2ce355f2-cab8-461c-9574-a586e47cad29" /># Secure AI Gateway

A self-hosted security gateway that intercepts every prompt before it reaches a local LLM — Keycloak IAM, JWT authentication, role-based access control, a threat detection engine, and a SOC-style monitoring dashboard.

> LLMs should never receive unvalidated input directly from users.

---
![Upload<svg width="100%" viewBox="0 0 707.55 740" role="img" style="" xmlns="http://www.w3.org/2000/svg">
  <title style="fill:rgb(0, 0, 0);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">Secure AI Gateway architecture diagram</title>
  <desc style="fill:rgb(0, 0, 0);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">Architecture showing the full request flow from Streamlit dashboard through Keycloak auth, FastAPI backend, threat detection, and Ollama inference, with audit logging to a database.</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  <mask id="imagine-text-gaps-61nh0r" maskUnits="userSpaceOnUse"><rect x="0" y="0" width="707.55" height="740" fill="white"/><rect x="-1.9762904644012451" y="70.30471801757812" width="60.69820785522461" height="19.2038516998291" fill="black" rx="2"/><rect x="8.860108375549316" y="210.3047332763672" width="38.1270809173584" height="19.2038516998291" fill="black" rx="2"/><rect x="-0.46869707107543945" y="386.3047180175781" width="57.66838836669922" height="19.2038516998291" fill="black" rx="2"/><rect x="-3.1001328229904175" y="576.3046875" width="63.434059143066406" height="19.2038516998291" fill="black" rx="2"/><rect x="1.121129035949707" y="678.3046875" width="53.82218551635742" height="19.2038516998291" fill="black" rx="2"/><rect x="68.07087707519531" y="62.228546142578125" width="127.27169799804688" height="21.542909622192383" fill="black" rx="2"/><rect x="71.25965881347656" y="83.39806365966797" width="122.32118225097656" height="19.2038516998291" fill="black" rx="2"/><rect x="272.1328430175781" y="62.228546142578125" width="135.13927459716797" height="21.542909622192383" fill="black" rx="2"/><rect x="288.0128173828125" y="83.39806365966797" width="104.82615661621094" height="19.2038516998291" fill="black" rx="2"/><rect x="496.4788513183594" y="62.228546142578125" width="104.05918884277344" height="21.542909622192383" fill="black" rx="2"/><rect x="496.24127197265625" y="83.39806365966797" width="104.75373840332031" height="19.2038516998291" fill="black" rx="2"/><rect x="290.4889221191406" y="168.22854614257812" width="99.77899932861328" height="21.542905807495117" fill="black" rx="2"/><rect x="228.732421875" y="189.3980712890625" width="222.1795654296875" height="19.2038516998291" fill="black" rx="2"/><rect x="284.4859619140625" y="226.30471801757812" width="110.86701965332031" height="19.2038516998291" fill="black" rx="2"/><rect x="281.1327209472656" y="270.2285461425781" width="118.95559692382812" height="21.542905807495117" fill="black" rx="2"/><rect x="209.2524871826172" y="291.3980712890625" width="261.1709899902344" height="19.2038516998291" fill="black" rx="2"/><rect x="240.0918426513672" y="331.3047180175781" width="79.47156524658203" height="19.2038516998291" fill="black" rx="2"/><rect x="255.0010986328125" y="370.2285461425781" width="169.99734497070312" height="21.542905807495117" fill="black" rx="2"/><rect x="223.48782348632812" y="391.3980712890625" width="234.66571044921875" height="19.2038516998291" fill="black" rx="2"/><rect x="95.68365478515625" y="368.3047180175781" width="68.4013557434082" height="19.2038516998291" fill="black" rx="2"/><rect x="90.20137786865234" y="471.228515625" width="62.18172836303711" height="21.542905807495117" fill="black" rx="2"/><rect x="85.72428131103516" y="487.3980712890625" width="72.05558776855469" height="19.2038516998291" fill="black" rx="2"/><rect x="425.68365478515625" y="408.3046875" width="68.4013557434082" height="19.2038516998291" fill="black" rx="2"/><rect x="270.3876953125" y="520.228515625" width="139.64706420898438" height="21.542905807495117" fill="black" rx="2"/><rect x="246.4489288330078" y="541.3980102539062" width="187.92710876464844" height="19.2038516998291" fill="black" rx="2"/><rect x="531.6764526367188" y="401.3046875" width="61.880157470703125" height="19.2038516998291" fill="black" rx="2"/><rect x="138.88368225097656" y="570.3046875" width="73.55547332763672" height="19.2038516998291" fill="black" rx="2"/><rect x="319.49993896484375" y="610.3047485351562" width="73.17108154296875" height="19.2038516998291" fill="black" rx="2"/><rect x="254.516845703125" y="670.228515625" width="169.94654846191406" height="21.542905807495117" fill="black" rx="2"/><rect x="214.41485595703125" y="691.3980712890625" width="250.8455810546875" height="19.2038516998291" fill="black" rx="2"/><rect x="561.6566772460938" y="476.3046875" width="140.2473602294922" height="19.2038516998291" fill="black" rx="2"/></mask></defs>

  <!-- ── LAYER LABELS (left margin) ────────────────────────────── -->
  <text x="28" y="84" text-anchor="middle" transform="rotate(-90,28,84)" opacity="0.5" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.5;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">Frontend</text>
  <text x="28" y="224" text-anchor="middle" transform="rotate(-90,28,224)" opacity="0.5" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.5;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">Auth</text>
  <text x="28" y="400" text-anchor="middle" transform="rotate(-90,28,400)" opacity="0.5" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.5;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">Backend</text>
  <text x="28" y="590" text-anchor="middle" transform="rotate(-90,28,590)" opacity="0.5" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.5;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">Inference</text>
  <text x="28" y="692" text-anchor="middle" transform="rotate(-90,28,692)" opacity="0.5" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.5;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">Storage</text>

  <!-- ── HORIZONTAL DIVIDERS ────────────────────────────────────── -->
  <line x1="50" y1="136" x2="640" y2="136" stroke="var(--color-border-tertiary)" stroke-width="0.5" stroke-dasharray="4 4" style="fill:rgb(0, 0, 0);stroke:rgba(31, 30, 29, 0.15);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-dasharray:4px, 4px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <line x1="50" y1="300" x2="640" y2="300" stroke="var(--color-border-tertiary)" stroke-width="0.5" stroke-dasharray="4 4" mask="url(#imagine-text-gaps-61nh0r)" style="fill:rgb(0, 0, 0);stroke:rgba(31, 30, 29, 0.15);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-dasharray:4px, 4px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <line x1="50" y1="490" x2="640" y2="490" stroke="var(--color-border-tertiary)" stroke-width="0.5" stroke-dasharray="4 4" mask="url(#imagine-text-gaps-61nh0r)" style="fill:rgb(0, 0, 0);stroke:rgba(31, 30, 29, 0.15);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-dasharray:4px, 4px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <line x1="50" y1="648" x2="640" y2="648" stroke="var(--color-border-tertiary)" stroke-width="0.5" stroke-dasharray="4 4" style="fill:rgb(0, 0, 0);stroke:rgba(31, 30, 29, 0.15);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-dasharray:4px, 4px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- ══════════════════════════════════════════════
       TIER 1 — STREAMLIT DASHBOARD (three role views)
  ══════════════════════════════════════════════ -->
  <!-- Admin -->
  <g onclick="sendPrompt('Tell me more about the admin dashboard')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="58" y="52" width="148" height="56" rx="8" stroke-width="0.5" style="fill:rgb(238, 237, 254);stroke:rgb(83, 74, 183);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="132" y="73" text-anchor="middle" dominant-baseline="central" style="fill:rgb(60, 52, 137);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Admin dashboard</text>
    <text x="132" y="93" text-anchor="middle" dominant-baseline="central" style="fill:rgb(83, 74, 183);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Metrics, charts, logs</text>
  </g>
  <!-- Analyst -->
  <g onclick="sendPrompt('Tell me more about the analyst dashboard')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="266" y="52" width="148" height="56" rx="8" stroke-width="0.5" style="fill:rgb(238, 237, 254);stroke:rgb(83, 74, 183);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="73" text-anchor="middle" dominant-baseline="central" style="fill:rgb(60, 52, 137);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Analyst dashboard</text>
    <text x="340" y="93" text-anchor="middle" dominant-baseline="central" style="fill:rgb(83, 74, 183);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Blocked prompts</text>
  </g>
  <!-- User -->
  <g onclick="sendPrompt('Tell me more about the user AI assistant view')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="474" y="52" width="148" height="56" rx="8" stroke-width="0.5" style="fill:rgb(238, 237, 254);stroke:rgb(83, 74, 183);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="548" y="73" text-anchor="middle" dominant-baseline="central" style="fill:rgb(60, 52, 137);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">User assistant</text>
    <text x="548" y="93" text-anchor="middle" dominant-baseline="central" style="fill:rgb(83, 74, 183);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Prompt interface</text>
  </g>

  <!-- ══════════════════════════════════════════════
       TIER 2 — KEYCLOAK AUTH
  ══════════════════════════════════════════════ -->
  <!-- Login form arrow down from dashboards -->
  <line x1="132" y1="108" x2="132" y2="158" marker-end="url(#arrow)" stroke="var(--color-border-secondary)" style="fill:none;stroke:rgb(115, 114, 108);color:rgb(0, 0, 0);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <line x1="340" y1="108" x2="340" y2="158" marker-end="url(#arrow)" stroke="var(--color-border-secondary)" style="fill:none;stroke:rgb(115, 114, 108);color:rgb(0, 0, 0);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <line x1="548" y1="108" x2="548" y2="158" marker-end="url(#arrow)" stroke="var(--color-border-secondary)" style="fill:none;stroke:rgb(115, 114, 108);color:rgb(0, 0, 0);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- Keycloak box -->
  <g onclick="sendPrompt('How does Keycloak JWT authentication work in this system?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="190" y="158" width="300" height="56" rx="8" stroke-width="0.5" style="fill:rgb(225, 245, 238);stroke:rgb(15, 110, 86);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="179" text-anchor="middle" dominant-baseline="central" style="fill:rgb(8, 80, 65);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Keycloak IAM</text>
    <text x="340" y="199" text-anchor="middle" dominant-baseline="central" style="fill:rgb(15, 110, 86);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">JWT RS256 · realm roles · client secret</text>
  </g>

  <!-- Converging arrows into Keycloak -->
  <path d="M132 146 L132 186 L190 186" fill="none" stroke="var(--color-border-secondary)" stroke-width="1" marker-end="url(#arrow)" style="fill:none;stroke:rgba(31, 30, 29, 0.3);color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <line x1="340" y1="146" x2="340" y2="158" fill="none" stroke="var(--color-border-secondary)" stroke-width="1" marker-end="url(#arrow)" style="fill:none;stroke:rgba(31, 30, 29, 0.3);color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <path d="M548 146 L548 186 L490 186" fill="none" stroke="var(--color-border-secondary)" stroke-width="1" marker-end="url(#arrow)" style="fill:none;stroke:rgba(31, 30, 29, 0.3);color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- JWT token label -->
  <text x="340" y="240" text-anchor="middle" opacity="0.6" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.6;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">JWT bearer token</text>
  <line x1="340" y1="214" x2="340" y2="260" marker-end="url(#arrow)" stroke="var(--color-border-secondary)" mask="url(#imagine-text-gaps-61nh0r)" style="fill:none;stroke:rgb(115, 114, 108);color:rgb(0, 0, 0);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- ══════════════════════════════════════════════
       TIER 3 — FASTAPI BACKEND
  ══════════════════════════════════════════════ -->

  <!-- FastAPI gateway box -->
  <g onclick="sendPrompt('What does the FastAPI gateway do?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="190" y="260" width="300" height="56" rx="8" stroke-width="0.5" style="fill:rgb(230, 241, 251);stroke:rgb(24, 95, 165);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="281" text-anchor="middle" dominant-baseline="central" style="fill:rgb(12, 68, 124);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">FastAPI gateway</text>
    <text x="340" y="301" text-anchor="middle" dominant-baseline="central" style="fill:rgb(24, 95, 165);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Token verify · RBAC · route /chat /audit /stats</text>
  </g>

  <!-- Arrow down into threat engine -->
  <text x="280" y="345" text-anchor="middle" opacity="0.6" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.6;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">user prompt</text>
  <line x1="340" y1="316" x2="340" y2="360" marker-end="url(#arrow)" stroke="var(--color-border-secondary)" style="fill:none;stroke:rgb(115, 114, 108);color:rgb(0, 0, 0);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- Threat detection box -->
  <g onclick="sendPrompt('How does the prompt injection detection work?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="190" y="360" width="300" height="56" rx="8" stroke-width="0.5" style="fill:rgb(250, 236, 231);stroke:rgb(153, 60, 29);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="381" text-anchor="middle" dominant-baseline="central" style="fill:rgb(113, 43, 19);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Threat detection engine</text>
    <text x="340" y="401" text-anchor="middle" dominant-baseline="central" style="fill:rgb(153, 60, 29);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Pattern match · risk score · severity level</text>
  </g>

  <!-- BLOCK branch (left) -->
  <path d="M190 388 L100 388 L100 460" fill="none" stroke="var(--color-border-secondary)" stroke-width="1" marker-end="url(#arrow)" style="fill:none;stroke:rgba(31, 30, 29, 0.3);color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="130" y="382" text-anchor="middle" opacity="0.6" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.6;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">score ≥ 80</text>

  <!-- BLOCKED box -->
  <g onclick="sendPrompt('What happens when a prompt is blocked?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="58" y="460" width="126" height="44" rx="8" stroke-width="0.5" style="fill:rgb(252, 235, 235);stroke:rgb(163, 45, 45);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="121" y="482" text-anchor="middle" dominant-baseline="central" style="fill:rgb(121, 31, 31);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Blocked</text>
    <text x="121" y="497" text-anchor="middle" dominant-baseline="central" style="fill:rgb(163, 45, 45);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Return 403</text>
  </g>

  <!-- ALLOW branch (right) — straight down -->
  <text x="375" y="422" text-anchor="middle" opacity="0.6" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.6;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">score &lt; 80</text>
  <line x1="340" y1="416" x2="340" y2="510" marker-end="url(#arrow)" stroke="var(--color-border-secondary)" style="fill:none;stroke:rgb(115, 114, 108);color:rgb(0, 0, 0);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- ══════════════════════════════════════════════
       TIER 4 — OLLAMA + TINYLLAMA
  ══════════════════════════════════════════════ -->
  <g onclick="sendPrompt('How does Ollama TinyLlama inference work?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="190" y="510" width="300" height="56" rx="8" stroke-width="0.5" style="fill:rgb(234, 243, 222);stroke:rgb(59, 109, 17);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="531" text-anchor="middle" dominant-baseline="central" style="fill:rgb(39, 80, 10);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Ollama + TinyLlama</text>
    <text x="340" y="551" text-anchor="middle" dominant-baseline="central" style="fill:rgb(59, 109, 17);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Local LLM inference · port 11434</text>
  </g>

  <!-- Response back up arrow -->
  <path d="M496 510 L540 510 L540 316 L496 316" fill="none" stroke="var(--color-border-secondary)" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arrow)" mask="url(#imagine-text-gaps-61nh0r)" style="fill:none;stroke:rgba(31, 30, 29, 0.3);color:rgb(0, 0, 0);stroke-width:1px;stroke-dasharray:4px, 3px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="562" y="415" text-anchor="middle" opacity="0.6" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.6;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">response</text>

  <!-- ══════════════════════════════════════════════
       TIER 5 — AUDIT LOG DATABASE
  ══════════════════════════════════════════════ -->
  <!-- Arrow from threat engine to DB (allowed) -->
  <path d="M340 566 L340 660" fill="none" stroke="var(--color-border-secondary)" stroke-width="1" marker-end="url(#arrow)" mask="url(#imagine-text-gaps-61nh0r)" style="fill:none;stroke:rgba(31, 30, 29, 0.3);color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <!-- Arrow from blocked box to DB -->
  <path d="M121 504 L121 660 L230 660" fill="none" stroke="var(--color-border-secondary)" stroke-width="1" marker-end="url(#arrow)" stroke-dasharray="4 3" mask="url(#imagine-text-gaps-61nh0r)" style="fill:none;stroke:rgba(31, 30, 29, 0.3);color:rgb(0, 0, 0);stroke-width:1px;stroke-dasharray:4px, 3px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <text x="175" y="584" text-anchor="middle" opacity="0.5" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.5;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">blocked log</text>
  <text x="356" y="624" text-anchor="middle" opacity="0.5" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.5;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">allowed log</text>

  <g onclick="sendPrompt('What does the audit log store?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="190" y="660" width="300" height="56" rx="8" stroke-width="0.5" style="fill:rgb(241, 239, 232);stroke:rgb(95, 94, 90);color:rgb(0, 0, 0);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="681" text-anchor="middle" dominant-baseline="central" style="fill:rgb(68, 68, 65);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Audit log (SQLAlchemy)</text>
    <text x="340" y="701" text-anchor="middle" dominant-baseline="central" style="fill:rgb(95, 94, 90);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">timestamp · user · prompt · severity · status</text>
  </g>

  <!-- Stats query arrow from DB back up to FastAPI -->
  <path d="M496 688 L610 688 L610 288 L496 288" fill="none" stroke="var(--color-border-secondary)" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arrow)" mask="url(#imagine-text-gaps-61nh0r)" style="fill:none;stroke:rgba(31, 30, 29, 0.3);color:rgb(0, 0, 0);stroke-width:1px;stroke-dasharray:4px, 3px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="632" y="490" text-anchor="middle" transform="rotate(-90,632,490)" opacity="0.5" style="fill:rgb(61, 61, 58);stroke:none;color:rgb(0, 0, 0);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:0.5;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">/stats · /audit · /blocked</text>

</svg>ing secure_ai_gateway_architecture_1.svg…]()

## What It Does

The gateway sits between users and a locally hosted language model (TinyLlama via Ollama). Every prompt is authenticated, authorised, scored for risk, then either blocked or forwarded — with every decision logged and surfaced through a role-specific dashboard.

```
User Prompt
    ↓
Keycloak Authentication  (JWT · RS256)
    ↓
RBAC Authorisation  (admin / analyst / user)
    ↓
Prompt Injection Detection + Risk Scoring
    ↓
Score ≥ 80 → BLOCKED ──→ Audit Log
Score < 80 → Ollama / TinyLlama Inference
                ↓
           Response + Audit Log
```

---

## Demo Videos

### Admin Dashboard

[Admin-Login-Dashboard.webm](https://github.com/user-attachments/assets/07daf403-a174-498e-b61c-0190fa674057)

Shows:
* Full SOC-style dashboard
* Metrics and visualisations
* Audit monitoring
* User activity analytics

---

### Analyst Dashboard

[Analyst-Login-Dashboard.webm](https://github.com/user-attachments/assets/7c06ed2a-8600-420f-a840-3e2bee21619e)

Shows:
* Threat monitoring workflow
* Blocked prompt visibility
* Security-focused analyst interface

---

### Allowed Prompt Flow

[Employee1-Login-Allowed-Prompt.webm](https://github.com/user-attachments/assets/c506feac-a959-4cfd-847b-1cafe513a7fc)

Shows:
* Successful authenticated inference
* Risk scoring and severity classification
* TinyLlama response generation

---

### Blocked Prompt Detection

[Employee1-Login-Blocked-Prompt-1.webm](https://github.com/user-attachments/assets/5809bcd5-ce72-462d-ad18-f08c52757c4f)

[Employee1-Login-Blocked-Prompt-2.webm](https://github.com/user-attachments/assets/adcf890a-76b5-47e6-bf61-c313901fcb08)

Shows:
* Prompt injection detection
* Real-time risk scoring
* Automatic blocking of high-risk prompts
* Audit logging of attacks

---

### Failed Login Attempt

[Failed-Login-Wrong-Password.webm](https://github.com/user-attachments/assets/31fe7a8b-e8c5-4ce0-9748-8e392ad84b64)

Shows:
* Authentication enforcement through Keycloak
* Rejection of invalid credentials

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend API | FastAPI |
| Authentication | Keycloak (IAM) + JWT (RS256) |
| Authorisation | Realm Roles via RBAC |
| AI Inference | Ollama + TinyLlama |
| Database | SQLAlchemy (PostgreSQL / SQLite) |
| Frontend Dashboard | Streamlit |
| Data Visualisation | Pandas + Matplotlib |
| Deployment | Oracle Cloud VM (Ubuntu) |
| Language | Python 3 |

---

## Features

- **JWT Authentication** — Keycloak issues RS256-signed tokens; the backend fetches the public JWKS to verify every request.
- **Role-Based Access Control** — `admin`, `analyst`, and `user` roles enforced at the API layer (FastAPI) and UI layer (Streamlit). Each role sees a different dashboard.
- **Prompt Injection Detection** — prompts are normalised (lowercased, punctuation stripped, spaces removed) then matched against a weighted pattern dictionary. Scores are summed and capped at 100.
- **Severity Classification** — every request is classified as `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL` based on its risk score.
- **Secure Inference** — only prompts scoring below 80 reach TinyLlama. Responses are trimmed to 500 characters.
- **Full Audit Logging** — every request is persisted with timestamp, username, prompt, status, risk score, severity, and detected patterns.
- **SOC-style Dashboard** — role-specific Streamlit views with metrics, charts, filterable audit tables, and a chat interface.

---

## API Endpoints

| Method | Endpoint | Roles | Description |
|---|---|---|---|
| `GET` | `/` | Public | Health check |
| `POST` | `/chat` | admin, analyst, user | Submit prompt — threat detection, then inference if clean |
| `GET` | `/audit` | admin, analyst | Full audit log |
| `GET` | `/blocked` | admin, analyst | Blocked prompts with detected patterns |
| `GET` | `/stats` | admin, analyst | Aggregated metrics, severity distribution, top users, request timeline |

### Example: Allowed Response

```json
{
  "success": true,
  "model": "tinyllama",
  "blocked": false,
  "risk_score": 0,
  "severity": "LOW",
  "response": "A firewall is a network security system that monitors..."
}
```

### Example: Blocked Response

```json
{
  "success": false,
  "blocked": true,
  "risk_score": 95,
  "severity": "CRITICAL",
  "detected_patterns": ["jailbreak"],
  "reason": "Prompt blocked due to security policy"
}
```

---

## Threat Detection Engine

Prompts are normalised before matching — lowercased, all non-alphanumeric characters stripped, spaces removed. This defeats trivial bypasses like `byp@ss security` or `JAILBREAK`. Pattern scores are summed and capped at 100.

Threat patterns map to [MITRE ATLAS](https://atlas.mitre.org/) techniques AML.T0051 (LLM Prompt Injection), AML.T0054 (LLM Jailbreak), and AML.T0056 (LLM Meta Prompt Extraction).

| Pattern | Risk Score |
|---|---|
| `bypass security` | 100 |
| `system override` | 100 |
| `reveal system prompt` | 95 |
| `jailbreak` | 95 |
| `ignore previous instructions` | 90 |
| `pretend to be root` | 90 |
| `disable safety` | 85 |
| `forget previous instructions` | 80 |
| `act as administrator` | 75 |

| Score Range | Severity | Action |
|---|---|---|
| 80 – 100 | CRITICAL | Blocked, logged |
| 50 – 79 | HIGH | Allowed, logged |
| 20 – 49 | MEDIUM | Allowed, logged |
| 0 – 19 | LOW | Allowed, logged |

---

## Dashboard Views

The Streamlit app authenticates against Keycloak directly — it calls the token endpoint, decodes the JWT to extract realm roles, and renders the appropriate view.

**Admin** — total requests, allowed, blocked, and critical attack counts; pie chart of allowed vs blocked; severity bar chart; top 5 active users; request volume over time; filterable audit and blocked prompt tables.

**Analyst** — blocked prompt log with full attack metadata: prompt, patterns, risk score, severity, timestamp.

**User** — prompt input and response display with risk score and severity classification.

---

## Architecture

**Frontend (Streamlit)** — three dashboard views rendered from the authenticated user's Keycloak realm role.

**Auth (Keycloak)** — issues a signed JWT (RS256) on login. The token travels as a Bearer header on every API call. The backend caches the public JWKS (`lru_cache`) and verifies the signature on each request.

**Backend (FastAPI)** — verifies the token, enforces RBAC, then passes the prompt to the threat detection engine: normalised, pattern-matched, scored. Prompts scoring ≥ 80 are blocked and logged. The rest go to inference.

**Inference (Ollama + TinyLlama)** — clean prompts forward to Ollama on port `11434`. Responses are trimmed to 500 characters and returned with the risk score and severity.

**Storage (SQLAlchemy)** — every request is persisted to the audit log. This table feeds `/audit`, `/blocked`, and `/stats`.

---

## Design Decisions

**Why normalise before matching?** Raw string matching is trivially bypassed — `JAILBREAK`, `j4ilbreak`, `jailbreak!` all evade a case-sensitive exact match. Normalisation collapses most surface-level obfuscation before the pattern check runs.

**Why cache the JWKS?** The public key doesn't change per request. Fetching it from Keycloak on every API call adds latency and a network dependency in the hot path. `lru_cache(maxsize=1)` fetches it once.

**Why block at ≥ 80?** `act as administrator` scores 75 — that phrase appears in legitimate prompts about IAM or system design. The threshold at 80 tolerates ambiguous language while blocking high-confidence attack patterns.

---

## Setup & Installation

### Prerequisites

- Python 3.9+
- [Keycloak](https://www.keycloak.org/) on port `8080`
- [Ollama](https://ollama.com/) running locally with TinyLlama pulled (`ollama pull tinyllama`)
- PostgreSQL or SQLite

### 1. Clone and Install

```bash
git clone https://github.com/your-username/secure-ai-gateway.git
cd secure-ai-gateway
pip install -r requirements.txt
```

### 2. Configure Keycloak

- Create a realm: `secure-ai`
- Create a client: `secure-ai-gateway`
- Create realm roles: `admin`, `analyst`, `user`
- Assign roles to users

### 3. Environment Variables

```env
# Backend (main.py)
KEYCLOAK_BASE_URL=
DATABASE_URL=

# Frontend (dashboard.py)
BASE_URL=
KEYCLOAK_URL=
REALM=
CLIENT_ID=
CLIENT_SECRET=
```

### 4. Run

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
streamlit run dashboard.py --server.port 8501
```

Background deployment on Linux:

```bash
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
nohup streamlit run dashboard.py --server.port 8501 &
```

---

## System Screenshots

### Infrastructure Overview

![Infrastructure Overview](./Screenshots/Infrastructure-System-Working-1.png)

---

### Filtering Logs by Username and Severity

![Filtering Logs](./Screenshots/Filtering-Logs-Using-Username-Severity.png)

---

### Keycloak Realm Configuration

![Keycloak Realm](./Screenshots/Keycloak-Realm-secure-ai.png)

---

### Keycloak Gateway Client

![Gateway Client](./Screenshots/Keycloak-gateway-secure-ai-gateway.png)

---

### Realm Roles

![Realm Roles](./Screenshots/Keycloak-Realm-Roles.png)

---

### User Management

![User Management](./Screenshots/Keycloak-Realm-User.png)

---

### Session Details

![Session Details](./Screenshots/Keycloak-Realm-Session-Detail.png)

---

## Key Takeaways

The core challenge wasn't the code — it was understanding why each layer exists. JWT verification needs JWKS caching because fetching the public key on every request puts a network call in your hot path. The block threshold sits at 80, not 100, because `act as administrator` appears in legitimate IAM prompts. Normalising before pattern matching closes the gap between `jailbreak` and `j4ilbreak`. Each decision has a reason, and the reason comes from how these systems fail in production.

The multi-service environment mattered too. Running Keycloak, FastAPI, Ollama, and Streamlit on a single Oracle Cloud VM — managing ports, background processes, and service dependencies — is a different problem from writing the application code.

---

## Real-World Relevance

Prompt injection is an active attack vector. As teams embed LLMs into internal tooling, attackers craft inputs to override system instructions, extract data, or bypass content policies. A gateway that normalises, scores, and blocks before inference is the pattern production AI security tools use - and the threats map directly to [MITRE ATLAS](https://atlas.mitre.org/) techniques AML.T0051, AML.T0054, and AML.T0056.

Most enterprise platforms handling sensitive data can't send it to an external API. Legal constraints, data residency requirements, and compliance obligations push organisations toward self-hosted inference. Running a local model behind an authenticated, audited gateway reflects how those deployments work.

RBAC and audit logging aren't features — they're the baseline for anything touching regulated data. Every request logged with a user, a timestamp, a risk score, and a disposition is the starting point for AI governance, which regulators are beginning to require explicitly.
