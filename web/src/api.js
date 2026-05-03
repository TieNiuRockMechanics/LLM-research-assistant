const BASE = '/api';

export async function listConversations() {
  const r = await fetch(`${BASE}/conversations`);
  if (!r.ok) throw new Error('Failed to list conversations');
  return r.json();
}

export async function getConversation(id) {
  const r = await fetch(`${BASE}/conversations/${id}`);
  if (!r.ok) throw new Error('Conversation not found');
  return r.json();
}

export async function deleteConversation(id) {
  await fetch(`${BASE}/conversations/${id}`, { method: 'DELETE' });
}

export async function sendMessage(question, knowledgeMode, model) {
  const r = await fetch(`${BASE}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question, knowledge_mode: knowledgeMode, model }),
  });
  if (!r.ok) {
    const detail = await r.text();
    throw new Error(detail || 'Chat request failed');
  }
  return r.json();
}

export async function saveConversation(id, messages) {
  await fetch(`${BASE}/conversations/${id}/messages`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(messages),
  });
}

export async function getStatus() {
  const r = await fetch(`${BASE}/status`);
  if (!r.ok) throw new Error('Status check failed');
  return r.json();
}
