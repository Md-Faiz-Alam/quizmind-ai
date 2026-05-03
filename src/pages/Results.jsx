import { useLocation, useNavigate } from 'react-router-dom'

export default function Results() {
  const { state } = useLocation()
  const navigate = useNavigate()

  if (!state) {
    navigate('/dashboard')
    return null
  }

  const { score, total, timeTaken } = state
  const accuracy = Math.round((score / total) * 100)

  const getMessage = () => {
    if (accuracy >= 80) return { text: 'Excellent! 🎉', color: '#38a169' }
    if (accuracy >= 60) return { text: 'Good Job! 👍', color: '#667eea' }
    if (accuracy >= 40) return { text: 'Keep Practicing! 💪', color: '#dd6b20' }
    return { text: 'Need More Practice! 📚', color: '#e53e3e' }
  }

  const msg = getMessage()

  return (
    <div style={styles.page}>
      <div style={styles.nav}>
        <div style={styles.navLogo}>🧠 QuizMind AI</div>
      </div>

      <div style={styles.container}>
        <div style={styles.card}>
          <div style={styles.emoji}>
            {accuracy >= 80 ? '🏆' : accuracy >= 60 ? '⭐' : accuracy >= 40 ? '💪' : '📚'}
          </div>

          <h1 style={{ ...styles.message, color: msg.color }}>
            {msg.text}
          </h1>

          <div style={styles.scoreCircle}>
            <div style={styles.scoreNum}>{accuracy}%</div>
            <div style={styles.scoreLbl}>Accuracy</div>
          </div>

          <div style={styles.statsRow}>
            <div style={styles.statBox}>
              <div style={styles.statVal}>{score}</div>
              <div style={styles.statLbl}>Correct</div>
            </div>
            <div style={styles.statBox}>
              <div style={styles.statVal}>{total - score}</div>
              <div style={styles.statLbl}>Wrong</div>
            </div>
            <div style={styles.statBox}>
              <div style={styles.statVal}>{total}</div>
              <div style={styles.statLbl}>Total</div>
            </div>
            <div style={styles.statBox}>
              <div style={styles.statVal}>{timeTaken}s</div>
              <div style={styles.statLbl}>Time</div>
            </div>
          </div>

          {/* AI Suggestion */}
          <div style={styles.suggestion}>
            <div style={styles.suggestionTitle}>✦ AI Insight</div>
            <p style={styles.suggestionText}>
              {accuracy >= 80
                ? 'Outstanding performance! Try a harder topic to challenge yourself further.'
                : accuracy >= 60
                ? 'Good effort! Review the questions you got wrong and try again.'
                : accuracy >= 40
                ? 'Keep going! Focus on the explanations shown during the quiz.'
                : 'Start with the basics. Re-read the topic before attempting again.'}
            </p>
          </div>

          <div style={styles.btnRow}>
            <button
              style={styles.btnSecondary}
              onClick={() => navigate('/dashboard')}
            >
              Back to Dashboard
            </button>
            <button
              style={styles.btnPrimary}
              onClick={() => navigate('/analytics')}
            >
              View Analytics →
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

const styles = {
  page: { minHeight: '100vh', background: '#f0f2f5' },
  nav: {
    background: '#fff', padding: '1rem 2rem',
    boxShadow: '0 2px 8px rgba(0,0,0,0.08)'
  },
  navLogo: { fontSize: 20, fontWeight: 700 },
  container: { maxWidth: 500, margin: '0 auto', padding: '2rem 1rem' },
  card: {
    background: '#fff', borderRadius: 16, padding: '2rem',
    boxShadow: '0 2px 12px rgba(0,0,0,0.08)', textAlign: 'center'
  },
  emoji: { fontSize: 56, marginBottom: 8 },
  message: { fontSize: 24, fontWeight: 700, marginBottom: 24 },
  scoreCircle: {
    width: 120, height: 120, borderRadius: '50%',
    background: 'linear-gradient(135deg, #667eea, #764ba2)',
    display: 'flex', flexDirection: 'column',
    alignItems: 'center', justifyContent: 'center',
    margin: '0 auto 24px', color: '#fff'
  },
  scoreNum: { fontSize: 32, fontWeight: 700 },
  scoreLbl: { fontSize: 12, opacity: 0.9 },
  statsRow: {
    display: 'grid', gridTemplateColumns: 'repeat(4,1fr)',
    gap: 12, marginBottom: 24
  },
  statBox: {
    background: '#f0f2f5', borderRadius: 10, padding: '0.8rem'
  },
  statVal: { fontSize: 22, fontWeight: 700, color: '#667eea' },
  statLbl: { fontSize: 11, color: '#888', marginTop: 2 },
  suggestion: {
    background: '#eef2ff', borderRadius: 10, padding: '1rem',
    marginBottom: 24, textAlign: 'left',
    borderLeft: '4px solid #667eea'
  },
  suggestionTitle: { fontWeight: 600, marginBottom: 6, color: '#667eea' },
  suggestionText: { fontSize: 13, color: '#555', lineHeight: 1.6 },
  btnRow: { display: 'flex', gap: 12 },
  btnSecondary: {
    flex: 1, padding: '12px', background: '#f0f2f5',
    borderRadius: 10, fontSize: 14, fontWeight: 600
  },
  btnPrimary: {
    flex: 1, padding: '12px', background: '#667eea',
    color: '#fff', borderRadius: 10, fontSize: 14, fontWeight: 600
  }
}