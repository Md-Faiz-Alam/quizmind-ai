import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { api, auth } from '../lib/api'

export default function Login() {
  const navigate = useNavigate()
  const [isLogin, setIsLogin] = useState(true)
  const [form, setForm] = useState({ name: '', email: '', password: '' })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async () => {
    setLoading(true)
    setError('')
    try {
      const endpoint = isLogin ? '/auth/login' : '/auth/register'
      const data = isLogin
        ? { email: form.email, password: form.password }
        : { name: form.name, email: form.email, password: form.password }
      const res = await api.post(endpoint, data)
      if (res.success) {
        auth.setUser(res.user)
        navigate('/dashboard')
      } else {
        setError(res.error || 'Something went wrong')
      }
    } catch (e) {
      setError('Cannot connect to server')
    }
    setLoading(false)
  }

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <div style={styles.logo}>QuizMind AI</div>
        <p style={styles.sub}>
          {isLogin ? 'Login to continue' : 'Create your account'}
        </p>
        {!isLogin && (
          <input
            style={styles.input}
            placeholder="Full Name"
            value={form.name}
            onChange={e => setForm({ ...form, name: e.target.value })}
          />
        )}
        <input
          style={styles.input}
          placeholder="Email"
          type="email"
          value={form.email}
          onChange={e => setForm({ ...form, email: e.target.value })}
        />
        <input
          style={styles.input}
          placeholder="Password"
          type="password"
          value={form.password}
          onChange={e => setForm({ ...form, password: e.target.value })}
        />
        {error && <p style={styles.error}>{error}</p>}
        <button style={styles.btn} onClick={handleSubmit} disabled={loading}>
          {loading ? 'Please wait...' : isLogin ? 'Login' : 'Register'}
        </button>
        <p style={styles.toggle}>
          {isLogin ? "Don't have an account? " : "Already have an account? "}
          <span style={styles.link} onClick={() => { setIsLogin(!isLogin); setError('') }}>
            {isLogin ? 'Register' : 'Login'}
          </span>
        </p>
      </div>
    </div>
  )
}

const styles = {
  container: {
    minHeight: '100vh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
  },
  card: {
    background: '#fff',
    borderRadius: 16,
    padding: '2.5rem',
    width: '100%',
    maxWidth: 400,
    boxShadow: '0 20px 60px rgba(0,0,0,0.15)'
  },
  logo: { fontSize: 28, fontWeight: 700, textAlign: 'center', marginBottom: 8 },
  sub: { textAlign: 'center', color: '#666', marginBottom: 24, fontSize: 14 },
  input: {
    width: '100%',
    padding: '12px 16px',
    marginBottom: 12,
    border: '1.5px solid #e0e0e0',
    borderRadius: 8,
    fontSize: 14,
    outline: 'none',
    display: 'block'
  },
  btn: {
    width: '100%',
    padding: '13px',
    background: '#667eea',
    color: '#fff',
    borderRadius: 8,
    fontSize: 15,
    fontWeight: 600,
    marginTop: 8
  },
  error: { color: '#e53e3e', fontSize: 13, marginBottom: 8, textAlign: 'center' },
  toggle: { textAlign: 'center', marginTop: 16, fontSize: 14, color: '#666' },
  link: { color: '#667eea', fontWeight: 600, cursor: 'pointer' }
}