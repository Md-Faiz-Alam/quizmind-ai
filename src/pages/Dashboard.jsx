import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { api, auth } from '../lib/api'

export default function Dashboard() {
  const navigate = useNavigate()
  const user = auth.getUser()
  const [analytics, setAnalytics] = useState([])
  const [topics, setTopics] = useState([])
  const [subtopics, setSubtopics] = useState({})
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (!user) { navigate('/'); return }

    Promise.all([
      api.get(`/results/analytics/${user.id}`),
      api.get(`/results/topics/${user.id}`)
    ]).then(async ([analyticsData, topicsData]) => {
      setAnalytics(analyticsData)
      setTopics(topicsData)

      const subMap = {}
      for (const topic of topicsData) {
        const subs = await api.get(`/results/subtopics/${topic.id}`)
        subMap[topic.id] = subs
      }
      setSubtopics(subMap)
      setLoading(false)
    })
  }, [])

  const getAccuracy = (topicName) => {
    const found = analytics.find(a => a.topic === topicName)
    return found ? found.avg_accuracy : 0
  }

  const totalAttempts = analytics.reduce((s, a) => s + a.attempts, 0)
  const avgAccuracy = analytics.length
    ? Math.round(analytics.reduce((s, a) => s + a.avg_accuracy, 0) / analytics.length)
    : 0

  const topicIcons = {
    'Python': '🐍', 'SQL': '🗄️', 'DSA': '⚙️',
    'Machine Learning': '🧠', 'Statistics': '📊', 'Data Analysis': '📈'
  }

  if (loading) return <div style={styles.loading}>Loading...</div>

  return (
    <div style={styles.page}>
      <div style={styles.nav}>
        <div style={styles.navLogo}>🧠 QuizMind AI</div>
        <div style={styles.navRight}>
          <span style={styles.navName}>Hi, {user?.name}</span>
          <button style={styles.logoutBtn} onClick={() => { auth.logout(); navigate('/') }}>
            Logout
          </button>
        </div>
      </div>

      <div style={styles.container}>
        <div style={styles.statsRow}>
          <div style={styles.statCard}>
            <div style={styles.statVal}>{totalAttempts}</div>
            <div style={styles.statLbl}>Quizzes Taken</div>
          </div>
          <div style={styles.statCard}>
            <div style={styles.statVal}>{avgAccuracy}%</div>
            <div style={styles.statLbl}>Avg Accuracy</div>
          </div>
          <div style={styles.statCard}>
            <div style={styles.statVal}>{analytics.length}</div>
            <div style={styles.statLbl}>Topics Covered</div>
          </div>
          <div style={styles.statCard}>
            <div style={styles.statVal}>{analytics.length > 0 ? 'B+' : 'N/A'}</div>
            <div style={styles.statLbl}>AI Readiness</div>
          </div>
        </div>

        <h2 style={styles.sectionTitle}>Choose a Topic</h2>
        <div style={styles.topicsGrid}>
          {topics.map(topic => (
            <div key={topic.id} style={styles.topicCard}>
              <div style={styles.topicHeader}>
                <span style={styles.topicIcon}>{topicIcons[topic.name] || '📚'}</span>
                <div>
                  <div style={styles.topicName}>{topic.name}</div>
                  <div style={styles.topicMeta}>{topic.subtopic_count} subtopics</div>
                </div>
              </div>
              <div style={styles.progressBar}>
                <div style={{ ...styles.progressFill, width: `${getAccuracy(topic.name)}%` }} />
              </div>
              <div style={styles.subtopics}>
                {(subtopics[topic.id] || []).map(sub => (
                  <button
                    key={sub.id}
                    style={styles.subBtn}
                    onClick={() => navigate(`/quiz/${sub.id}`)}
                  >
                    {sub.name} →
                  </button>
                ))}
              </div>
            </div>
          ))}
        </div>

        <div style={styles.bottomNav}>
          <button style={styles.bottomBtn} onClick={() => navigate('/analytics')}>
            📊 View Analytics
          </button>
        </div>
      </div>
    </div>
  )
}

const styles = {
  page: { minHeight: '100vh', background: '#f0f2f5' },
  loading: { minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' },
  nav: {
    background: '#fff', padding: '1rem 2rem',
    display: 'flex', justifyContent: 'space-between',
    alignItems: 'center', boxShadow: '0 2px 8px rgba(0,0,0,0.08)'
  },
  navLogo: { fontSize: 20, fontWeight: 700 },
  navRight: { display: 'flex', alignItems: 'center', gap: 12 },
  navName: { fontSize: 14, color: '#666' },
  logoutBtn: { padding: '6px 14px', background: '#f0f2f5', borderRadius: 8, fontSize: 13, fontWeight: 500 },
  container: { maxWidth: 900, margin: '0 auto', padding: '2rem 1rem' },
  statsRow: { display: 'grid', gridTemplateColumns: 'repeat(4,1fr)', gap: 12, marginBottom: 32 },
  statCard: { background: '#fff', borderRadius: 12, padding: '1.2rem', textAlign: 'center', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' },
  statVal: { fontSize: 28, fontWeight: 700, color: '#667eea' },
  statLbl: { fontSize: 12, color: '#888', marginTop: 4 },
  sectionTitle: { fontSize: 18, fontWeight: 600, marginBottom: 16 },
  topicsGrid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(260px,1fr))', gap: 16 },
  topicCard: { background: '#fff', borderRadius: 12, padding: '1.2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' },
  topicHeader: { display: 'flex', alignItems: 'center', gap: 12, marginBottom: 12 },
  topicIcon: { fontSize: 28 },
  topicName: { fontWeight: 600, fontSize: 15 },
  topicMeta: { fontSize: 12, color: '#888' },
  progressBar: { height: 6, background: '#f0f2f5', borderRadius: 3, marginBottom: 12 },
  progressFill: { height: 6, background: '#667eea', borderRadius: 3, transition: 'width 0.3s' },
  subtopics: { display: 'flex', flexDirection: 'column', gap: 6 },
  subBtn: { padding: '8px 12px', background: '#f0f2f5', borderRadius: 8, fontSize: 13, textAlign: 'left', fontWeight: 500 },
  bottomNav: { marginTop: 32, textAlign: 'center' },
  bottomBtn: { padding: '12px 32px', background: '#667eea', color: '#fff', borderRadius: 10, fontSize: 15, fontWeight: 600 }
}