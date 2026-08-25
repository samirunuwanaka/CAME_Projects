// AeroTrip AI Multi-Agent Frontend Orchestration & Animation
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('plan-form');
  const placeholder = document.getElementById('welcome-placeholder');
  const loader = document.getElementById('loading-overlay');
  const viewport = document.getElementById('content-viewport');
  const progressFill = document.getElementById('progress-fill');

  // Node Badges
  const badgeGuardrails = document.getElementById('badge-guardrails');
  const badgeFlight = document.getElementById('badge-flight');
  const badgePlaces = document.getElementById('badge-places');
  const badgeMaster = document.getElementById('badge-master');

  // Step Chips
  const chip1 = document.getElementById('chip-1');
  const chip2 = document.getElementById('chip-2');
  const chip3 = document.getElementById('chip-3');
  const chip4 = document.getElementById('chip-4');

  // Tab Navigation
  const navTabs = document.querySelectorAll('.nav-tab');
  const tabPanels = document.querySelectorAll('.tab-panel');

  // Markdown Viewports
  const masterMd = document.getElementById('master-md');
  const flightsMd = document.getElementById('flights-md');
  const placesMd = document.getElementById('places-md');
  const hotelsMd = document.getElementById('hotels-md');
  const guardrailsMd = document.getElementById('guardrails-md');
  const budgetMd = document.getElementById('budget-md');

  // Chat Elements
  const chatStreamBox = document.getElementById('chat-stream-box');
  const userChatInput = document.getElementById('user-chat-input');
  const chatSendBtn = document.getElementById('chat-send-btn');

  // Tab Handler
  navTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      navTabs.forEach(t => t.classList.remove('active'));
      tabPanels.forEach(p => p.classList.remove('active'));

      tab.classList.add('active');
      const targetId = tab.getAttribute('data-tab');
      document.getElementById(targetId).classList.add('active');
    });
  });

  // Form Submit Handler
  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const origin = document.getElementById('origin').value.trim();
    const destination = document.getElementById('destination').value.trim();
    const duration_days = parseInt(document.getElementById('duration').value);
    const budget = parseFloat(document.getElementById('budget').value);
    const travel_purpose = document.getElementById('purpose').value.trim();
    const preferences = document.getElementById('preferences').value.trim();
    const passport_valid_months = parseInt(document.getElementById('passport-months').value);
    const visa_status = document.getElementById('visa-type').value;

    // Reset Viewports & Show Loader
    placeholder.classList.add('hidden');
    viewport.classList.add('hidden');
    loader.classList.remove('hidden');

    // Reset Node Badges
    badgeGuardrails.textContent = 'Checking';
    badgeGuardrails.className = 'node-status-badge badge-active';
    badgeFlight.textContent = 'Queued';
    badgeFlight.className = 'node-status-badge badge-standby';
    badgePlaces.textContent = 'Queued';
    badgePlaces.className = 'node-status-badge badge-standby';
    badgeMaster.textContent = 'Queued';
    badgeMaster.className = 'node-status-badge badge-standby';

    chip1.className = 'step-chip active-chip';
    chip2.className = 'step-chip';
    chip3.className = 'step-chip';
    chip4.className = 'step-chip';
    progressFill.style.width = '20%';

    // Step Animation Simulation
    setTimeout(() => {
      progressFill.style.width = '45%';
      badgeGuardrails.textContent = 'Verified 🛡️';
      badgeGuardrails.className = 'node-status-badge badge-ready';

      badgeFlight.textContent = 'Active 🛫';
      badgeFlight.className = 'node-status-badge badge-active';
      chip2.className = 'step-chip active-chip';
    }, 600);

    setTimeout(() => {
      progressFill.style.width = '70%';
      badgeFlight.textContent = 'Done ✅';
      badgeFlight.className = 'node-status-badge badge-ready';

      badgePlaces.textContent = 'Active 📍';
      badgePlaces.className = 'node-status-badge badge-active';
      chip3.className = 'step-chip active-chip';
    }, 1200);

    setTimeout(() => {
      progressFill.style.width = '90%';
      badgePlaces.textContent = 'Done ✅';
      badgePlaces.className = 'node-status-badge badge-ready';

      badgeMaster.textContent = 'Synthesizing 🤖';
      badgeMaster.className = 'node-status-badge badge-active';
      chip4.className = 'step-chip active-chip';
    }, 1800);

    try {
      const response = await fetch('/api/plan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          origin,
          destination,
          duration_days,
          budget,
          travel_purpose,
          preferences,
          passport_valid_months,
          visa_status,
        })
      });

      if (!response.ok) {
        throw new Error(`Server returned status: ${response.status}`);
      }

      const data = await response.json();

      const masterContent = `
# ✈️ Master Combined Travel Plan: ${data.trip.origin} ➔ ${data.trip.destination}

${data.guardrail_report}

---

## 🛫 Outbound & Inbound Flights (Flight Planner Sub-Agent)
${data.flight_suggestions}

${data.flight_prerequisites}

---

## 📍 Places to Visit & Dining (Places Explorer Sub-Agent)
${data.places_to_visit}

${data.dining_recommendations}

---

## 🏨 Lodging & Executive Stays
${data.hotel_recommendations}

---

## 📅 Day-by-Day Combined Itinerary
${data.master_itinerary}

---

## 📊 Budget & Prerequisites Summary
${data.budget_breakdown}

${data.prerequisites_checklist}
      `;

      masterMd.innerHTML = marked.parse(masterContent);
      flightsMd.innerHTML = marked.parse(`${data.flight_suggestions}\n\n${data.flight_prerequisites}`);
      placesMd.innerHTML = marked.parse(`${data.places_to_visit}\n\n${data.dining_recommendations}`);
      hotelsMd.innerHTML = marked.parse(data.hotel_recommendations);
      guardrailsMd.innerHTML = marked.parse(`${data.guardrail_report}\n\n${data.prerequisites_checklist}`);
      budgetMd.innerHTML = marked.parse(data.budget_breakdown);

      progressFill.style.width = '100%';
      badgeMaster.textContent = 'Complete 🌟';
      badgeMaster.className = 'node-status-badge badge-ready';

      setTimeout(() => {
        loader.classList.add('hidden');
        viewport.classList.remove('hidden');
      }, 400);

    } catch (err) {
      console.error(err);
      alert('Error running sub-agents: ' + err.message);
      loader.classList.add('hidden');
      placeholder.classList.remove('hidden');

      badgeGuardrails.textContent = 'Error';
      badgeFlight.textContent = 'Error';
      badgePlaces.textContent = 'Error';
      badgeMaster.textContent = 'Error';
    }
  });

  // Chat interaction
  const handleChat = () => {
    const text = userChatInput.value.trim();
    if (!text) return;

    const userBubble = document.createElement('div');
    userBubble.className = 'chat-bubble user-bubble';
    userBubble.innerHTML = `<div class="bubble-header" style="color: var(--color-cyan);">👤 You</div><p>${text}</p>`;
    chatStreamBox.appendChild(userBubble);
    userChatInput.value = '';

    chatStreamBox.scrollTop = chatStreamBox.scrollHeight;

    setTimeout(() => {
      const botBubble = document.createElement('div');
      botBubble.className = 'chat-bubble bot-bubble';
      botBubble.innerHTML = `<div class="bubble-header">🤖 AeroTrip AI Agent</div><p>I have received your request: <em>"${text}"</em>. I've instructed the Flight Planner and Places Explorer sub-agents to dynamically adjust your schedule while keeping within guardrails!</p>`;
      chatStreamBox.appendChild(botBubble);
      chatStreamBox.scrollTop = chatStreamBox.scrollHeight;
    }, 700);
  };

  chatSendBtn.addEventListener('click', handleChat);
  userChatInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') handleChat();
  });
});
