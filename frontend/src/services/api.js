/**
 * Centralized TRAVELENS API Service
 * Interacts with FastAPI backend REST endpoints.
 */

const API_BASE = '/api';

export const tokenStorage = {
  get: () => localStorage.getItem('travelens_token'),
  set: (token) => localStorage.setItem('travelens_token', token),
  clear: () => localStorage.removeItem('travelens_token'),
};

async function apiRequest(endpoint, options = {}) {
  const url = `${API_BASE}${endpoint}`;
  const headers = {
    'Content-Type': 'application/json',
    ...(options.headers || {}),
  };

  const token = tokenStorage.get();
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  try {
    const res = await fetch(url, { ...options, headers });
    if (!res.ok) {
      if (res.status === 401 && token) {
        tokenStorage.clear();
      }
      let errorDetail = `Request failed with status ${res.status}`;
      try {
        const errJson = await res.json();
        if (errJson.detail) {
          errorDetail = typeof errJson.detail === 'string' ? errJson.detail : JSON.stringify(errJson.detail);
        }
      } catch {
        // Fallback to status text
      }
      throw new Error(errorDetail);
    }
    return await res.json();
  } catch (err) {
    console.error(`[API Error] ${endpoint}:`, err);
    throw err;
  }
}

// Destination endpoints
export async function getDestinations(params = {}) {
  const query = new URLSearchParams();
  if (params.query) query.set('query', params.query);
  if (params.category && params.category !== 'All') query.set('category', params.category);
  if (params.region && params.region !== 'All') query.set('region', params.region);
  if (params.budget_tier && params.budget_tier !== 'All') query.set('budget_tier', params.budget_tier);
  if (params.sort_by) query.set('sort_by', params.sort_by);
  const qStr = query.toString();
  return apiRequest(`/destinations${qStr ? `?${qStr}` : ''}`);
}

export async function getDestinationById(id) {
  return apiRequest(`/destinations/${id}`);
}

export async function getDestinationAnalytics(id) {
  return apiRequest(`/destinations/${id}/analytics`);
}

export async function getDestinationTrends(id) {
  return apiRequest(`/destinations/${id}/trends`);
}

export async function getDestinationKeywords(id, topN = 10) {
  return apiRequest(`/destinations/${id}/keywords?top_n=${topN}`);
}

export async function getDestinationReviews(id, params = {}) {
  const query = new URLSearchParams();
  if (params.sentiment && params.sentiment !== 'All') query.set('sentiment', params.sentiment);
  if (params.rating && params.rating !== 'All') query.set('rating', params.rating);
  if (params.aspect && params.aspect !== 'All') query.set('aspect', params.aspect);
  const qStr = query.toString();
  return apiRequest(`/destinations/${id}/reviews${qStr ? `?${qStr}` : ''}`);
}

// Review Text Analysis
export async function analyzeReviewText(reviewText) {
  return apiRequest('/analyze-review', {
    method: 'POST',
    body: JSON.stringify({ review_text: reviewText }),
  });
}

// Model Metrics
export async function getModelMetrics() {
  return apiRequest('/analysis/model-metrics');
}

// Authentication
export async function loginUser(email, password) {
  const data = await apiRequest('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  });
  if (data.access_token) {
    tokenStorage.set(data.access_token);
  }
  return data;
}

export async function registerUser(name, email, password) {
  const data = await apiRequest('/auth/register', {
    method: 'POST',
    body: JSON.stringify({ name, email, password }),
  });
  if (data.access_token) {
    tokenStorage.set(data.access_token);
  }
  return data;
}

export async function getMe() {
  return apiRequest('/auth/me');
}

export function logoutUser() {
  tokenStorage.clear();
}

// Personalized Recommendations
export async function getRecommendations(priorities, topN = 6) {
  return apiRequest(`/recommendations?top_n=${topN}`, {
    method: 'POST',
    body: JSON.stringify(priorities),
  });
}

// Saved Destinations
export async function getSavedDestinations() {
  return apiRequest('/saved-destinations');
}

export async function saveDestination(destinationId) {
  return apiRequest(`/saved-destinations/${destinationId}`, {
    method: 'POST',
  });
}

export async function removeSavedDestination(destinationId) {
  return apiRequest(`/saved-destinations/${destinationId}`, {
    method: 'DELETE',
  });
}

export async function getSavedStatus(destinationId) {
  return apiRequest(`/saved-destinations/${destinationId}/status`);
}

// Issue Reporting and Data Integrity Feedback
export async function submitIssueReport(reportData) {
  return apiRequest('/feedback/report', {
    method: 'POST',
    body: JSON.stringify(reportData),
  });
}

