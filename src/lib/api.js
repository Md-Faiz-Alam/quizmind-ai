const BASE_URL = `${import.meta.env.VITE_API_URL}/api`;

export const api = {
  async get(endpoint) {
    const res = await fetch(`${BASE_URL}${endpoint}`);
    return res.json();
  },

  async post(endpoint, data) {
    const res = await fetch(`${BASE_URL}${endpoint}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    return res.json();
  },
};

export const auth = {
  getUser: () => JSON.parse(localStorage.getItem("user")),
  setUser: (user) => localStorage.setItem("user", JSON.stringify(user)),
  logout: () => localStorage.removeItem("user"),
  isLoggedIn: () => !!localStorage.getItem("user"),
};
