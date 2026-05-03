import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { api, auth } from '../lib/api'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'

export default function Analytics() {
  const navigate = useNavigate()
  const user = auth.getUser()
  const [analytics, setAnalytics] = useState([])
  const [weakAreas, setWeakAreas] = useState([])
  const [history, setHistory] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (!user) { navigate('/'); return }
    Promise.all([
      api.get(`/results/analytics/${user.id}`),
      api.get(`/results/weak-areas/${user.id}`),
      api.get(`/results/history/${user.id}`)
    ]).then(([a, w, h]) => {
      setAnalytics(a)
      setWeakAreas(w)
      setHistory(h)
      setLoading(false)
    })
  }, [])

  if (loading) return (
    <div style={styles.center}>Loading analytics...</div>
  )

  const chartData = analytics.map(a => ({
    name: a.topic,
    accuracy: a.avg_accuracy,
    attempts: a.attempts
  }))

  return (
    <div style={styles.page}>
      <div style={styles.nav}>
        <div style={styles.navLogo}>🧠 QuizMind AI</div>
        <div style={styles.navRight}>
          <button style={styles.backBtn} onClick={() => navigate('/dashboard')}>
            ← Dashboard
          </button>
        </div>
      </div>

      <div style={styles.container}>
        <h2 style={styles.title}>Your Performance Analytics</h2>

        {analytics.length === 0 ? (
          <div style={styles.emptyCard}>
            <p style={styles.emptyText}>No data yet! Take a quiz first.</p>
            <button style={styles.btn} onClick={() => navigate('/dashboard')}>
              Start a Quiz →
            </button>
          </div>
        ) : (
          <>
            {/* Stats Row */}
            <div style={styles.statsRow}>
              <div style={styles.statCard}>
                <div style={styles.statVal}>
                  {analytics.reduce((s, a) => s + a.attempts, 0)}
                </div>
                <div style={styles.statLbl}>Total Quizzes</div>
              </div>
              <div style={styles.statCard}>
                <div style={styles.statVal}>
                  {Math.round(analytics.reduce((s, a) => s + a.avg_accuracy, 0) / analytics.length)}%
                </div>
                <div style={styles.statLbl}>Overall Accuracy</div>
              </div>
              <div style={styles.statCard}>
                <div style={styles.statVal}>{analytics.length}</div>
                <div style={styles.statLbl}>Topics Attempted</div>
              </div>
              <div style={styles.statCard}>
                <div style={styles.statVal}>{weakAreas.length}</div>
                <div style={styles.statLbl}>Weak Areas</div>
              </div>
            </div>

            {/* Bar Chart */}
            <div style={styles.card}>
              <h3 style={styles.cardTitle}>Accuracy by Topic</h3>
              <ResponsiveContainer width="100%" height={250}>
                <BarChart data={chartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" tick={{ fontSize: 12 }} />
                  <YAxis domain={[0, 100]} tick={{ fontSize: 12 }} />
                  <Tooltip formatter={(val) => `${val}%`} />
                  <Bar dataKey="accuracy" fill="#667eea" radius={[6, 6, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>

            {/* Weak Areas */}
            {weakAreas.length > 0 && (
              <div style={styles.card}>
                <h3 style={styles.cardTitle}>⚠️ Weak Areas (below 60%)</h3>
                <div style={styles.weakList}>
                  {weakAreas.map((w, i) => (
                    <div key={i} style={styles.weakItem}>
                      <span style={styles.weakName}>{w.subtopic}</span>
                      <div style={styles.weakBar}>
                        <div style={{
                          ...styles.weakFill,
                          width: `${w.accuracy}%`,
                          background: w.accuracy < 40 ? '#e53e3e' : '#dd6b20'
                        }} />
                      </div>
                      <span style={styles.weakPct}>{w.accuracy}%</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* History */}
            {history.length > 0 && (
              <div style={styles.card}>
                <h3 style={styles.cardTitle}>Recent Quiz History</h3>
                <div style={styles.historyList}>
                  {history.slice(0, 5).map((h, i) => (
                    <div key={i} style={styles.historyItem}>
                      <div>
                        <div style={styles.historyTopic}>{h.subtopic}</div>
                        <div style={styles.historyDate}>{h.date?.slice(0, 10)}</div>
                      </div>
                      <div style={styles.historyRight}>
                        <span style={{
                          ...styles.accuracyBadge,
                          background: h.accuracy >= 60 ? '#c6f6d5' : '#fed7d7',
                          color: h.accuracy >= 60 ? '#276749' : '#c53030'
                        }}>
                          {h.accuracy}%
                        </span>
                        <span style={styles.historyScore}>
                          {h.score}/{h.total}
                        </span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* AI Study Plan */}
            <div style={styles.aiCard}>
              <div style={styles.aiTitle}>✦ AI Study Recommendation</div>
              <p style={styles.aiText}>
                {weakAreas.length > 0
                  ? `Focus on ${weakAreas[0].subtopic} — your accuracy is only ${weakAreas[0].accuracy}%. Practice 10 questions daily on this topic to improve within a week.`
                  : 'Great performance across all topics! Try System Design and Statistics to expand your knowledge further.'}
              </p>
            </div>
          </>
        )}
      </div>
    </div>
  )
}

const styles = {
  page: { minHeight: '100vh', background: '#f0f2f5' },
  center: { minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' },
  nav: {
    background: '#fff', padding: '1rem 2rem',
    display: 'flex', justifyContent: 'space-between',
    alignItems: 'center', boxShadow: '0 2px 8px rgba(0,0,0,0.08)'
  },
  navLogo: { fontSize: 20, fontWeight: 700 },
  navRight: { display: 'flex', gap: 12 },
  backBtn: { padding: '6px 14px', background: '#f0f2f5', borderRadius: 8, fontSize: 13, fontWeight: 500 },
  container: { maxWidth: 900, margin: '0 auto', padding: '2rem 1rem' },
  title: { fontSize: 22, fontWeight: 700, marginBottom: 24 },
  emptyCard: {
    background: '#fff', borderRadius: 16, padding: '3rem',
    textAlign: 'center', boxShadow: '0 2px 8px rgba(0,0,0,0.06)'
  },
  emptyText: { fontSize: 16, color: '#666', marginBottom: 16 },
  btn: { padding: '10px 24px', background: '#667eea', color: '#fff', borderRadius: 8, fontSize: 14, fontWeight: 600 },
  statsRow: { display: 'grid', gridTemplateColumns: 'repeat(4,1fr)', gap: 12, marginBottom: 20 },
  statCard: { background: '#fff', borderRadius: 12, padding: '1.2rem', textAlign: 'center', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' },
  statVal: { fontSize: 28, fontWeight: 700, color: '#667eea' },
  statLbl: { fontSize: 12, color: '#888', marginTop: 4 },
  card: { background: '#fff', borderRadius: 16, padding: '1.5rem', marginBottom: 20, boxShadow: '0 2px 8px rgba(0,0,0,0.06)' },
  cardTitle: { fontSize: 16, fontWeight: 600, marginBottom: 16 },
  weakList: { display: 'flex', flexDirection: 'column', gap: 12 },
  weakItem: { display: 'flex', alignItems: 'center', gap: 12 },
  weakName: { fontSize: 13, fontWeight: 500, minWidth: 100 },
  weakBar: { flex: 1, height: 8, background: '#f0f2f5', borderRadius: 4 },
  weakFill: { height: 8, borderRadius: 4 },
  weakPct: { fontSize: 13, fontWeight: 600, minWidth: 40, textAlign: 'right' },
  historyList: { display: 'flex', flexDirection: 'column', gap: 10 },
  historyItem: {
    display: 'flex', justifyContent: 'space-between',
    alignItems: 'center', padding: '10px 12px',
    background: '#f0f2f5', borderRadius: 8
  },
  historyTopic: { fontSize: 14, fontWeight: 500 },
  historyDate: { fontSize: 11, color: '#888', marginTop: 2 },
  historyRight: { display: 'flex', alignItems: 'center', gap: 10 },
  accuracyBadge: { fontSize: 12, fontWeight: 600, padding: '3px 10px', borderRadius: 20 },
  historyScore: { fontSize: 13, color: '#666' },
  aiCard: {
    background: '#eef2ff', borderRadius: 16, padding: '1.5rem',
    borderLeft: '4px solid #667eea'
  },
  aiTitle: { fontSize: 15, fontWeight: 600, color: '#667eea', marginBottom: 8 },
  aiText: { fontSize: 13, color: '#555', lineHeight: 1.7 }
}