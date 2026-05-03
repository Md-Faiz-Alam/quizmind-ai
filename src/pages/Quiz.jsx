import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api, auth } from '../lib/api'

export default function Quiz() {
  const { subtopicId } = useParams()
  const navigate = useNavigate()
  const user = auth.getUser()

  const [questions, setQuestions] = useState([])
  const [current, setCurrent] = useState(0)
  const [selected, setSelected] = useState(null)
  const [score, setScore] = useState(0)
  const [showExplanation, setShowExplanation] = useState(false)
  const [timer, setTimer] = useState(30)
  const [startTime] = useState(Date.now())
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.get(`/quiz/questions/${subtopicId}`).then(data => {
      setQuestions(data)
      setLoading(false)
    })
  }, [])

  useEffect(() => {
    if (selected !== null || loading) return
    const t = setInterval(() => {
      setTimer(prev => {
        if (prev <= 1) {
          clearInterval(t)
          handleNext()
          return 30
        }
        return prev - 1
      })
    }, 1000)
    return () => clearInterval(t)
  }, [current, selected, loading])

  const handleAnswer = (key) => {
    if (selected) return
    setSelected(key)
    setShowExplanation(true)
    if (key === questions[current].correct_answer) {
      setScore(s => s + 1)
    }
  }

  const handleNext = () => {
    if (current + 1 >= questions.length) {
      finishQuiz()
      return
    }
    setCurrent(c => c + 1)
    setSelected(null)
    setShowExplanation(false)
    setTimer(30)
  }

  const finishQuiz = async () => {
    const timeTaken = Math.round((Date.now() - startTime) / 1000)
    await api.post('/results/save', {
      user_id: user.id,
      subtopic_id: parseInt(subtopicId),
      score,
      total: questions.length,
      time_taken: timeTaken
    })
    navigate('/results', {
      state: { score, total: questions.length, timeTaken, subtopicId }
    })
  }

  if (loading) return (
    <div style={styles.center}>
      <p>Loading questions...</p>
    </div>
  )

  if (questions.length === 0) return (
    <div style={styles.center}>
      <p>No questions found for this topic.</p>
      <button style={styles.btn} onClick={() => navigate('/dashboard')}>
        Go Back
      </button>
    </div>
  )

  const q = questions[current]
  const optionColors = (key) => {
    if (!selected) return '#f0f2f5'
    if (key === q.correct_answer) return '#c6f6d5'
    if (key === selected && key !== q.correct_answer) return '#fed7d7'
    return '#f0f2f5'
  }

  return (
    <div style={styles.page}>
      <div style={styles.nav}>
        <div style={styles.navLogo}>🧠 QuizMind AI</div>
        <button style={styles.exitBtn} onClick={() => navigate('/dashboard')}>
          Exit Quiz
        </button>
      </div>

      <div style={styles.container}>
        {/* Progress */}
        <div style={styles.progressRow}>
          <span style={styles.progressText}>
            Question {current + 1} of {questions.length}
          </span>
          <span style={{ ...styles.timerBadge, background: timer <= 10 ? '#fed7d7' : '#eef2ff' }}>
            ⏱ {timer}s
          </span>
        </div>
        <div style={styles.progressBar}>
          <div style={{
            ...styles.progressFill,
            width: `${((current + 1) / questions.length) * 100}%`
          }} />
        </div>

        {/* Question */}
        <div style={styles.card}>
          <p style={styles.question}>{q.question}</p>

          <div style={styles.options}>
            {Object.entries(q.options).map(([key, val]) => (
              <button
                key={key}
                style={{ ...styles.option, background: optionColors(key) }}
                onClick={() => handleAnswer(key)}
                disabled={!!selected}
              >
                <span style={styles.optKey}>{key.toUpperCase()}</span>
                {val}
              </button>
            ))}
          </div>

          {/* Explanation */}
          {showExplanation && (
            <div style={styles.explanation}>
              <strong>💡 Explanation:</strong> {q.explanation}
            </div>
          )}

          {/* Next Button */}
          {selected && (
            <button style={styles.nextBtn} onClick={handleNext}>
              {current + 1 >= questions.length ? 'Finish Quiz' : 'Next Question →'}
            </button>
          )}
        </div>

        {/* Score */}
        <div style={styles.scoreBar}>
          ✅ Score: {score} / {current + 1}
        </div>
      </div>
    </div>
  )
}

const styles = {
  page: { minHeight: '100vh', background: '#f0f2f5' },
  center: { minHeight: '100vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 16 },
  nav: {
    background: '#fff', padding: '1rem 2rem',
    display: 'flex', justifyContent: 'space-between',
    alignItems: 'center', boxShadow: '0 2px 8px rgba(0,0,0,0.08)'
  },
  navLogo: { fontSize: 20, fontWeight: 700 },
  exitBtn: { padding: '6px 14px', background: '#fed7d7', borderRadius: 8, fontSize: 13, fontWeight: 500 },
  container: { maxWidth: 700, margin: '0 auto', padding: '2rem 1rem' },
  progressRow: { display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 },
  progressText: { fontSize: 14, color: '#666' },
  timerBadge: { fontSize: 13, fontWeight: 600, padding: '4px 12px', borderRadius: 20 },
  progressBar: { height: 8, background: '#e2e8f0', borderRadius: 4, marginBottom: 24 },
  progressFill: { height: 8, background: '#667eea', borderRadius: 4, transition: 'width 0.3s' },
  card: {
    background: '#fff', borderRadius: 16, padding: '2rem',
    boxShadow: '0 2px 12px rgba(0,0,0,0.08)'
  },
  question: { fontSize: 18, fontWeight: 600, marginBottom: 24, lineHeight: 1.5 },
  options: { display: 'flex', flexDirection: 'column', gap: 10 },
  option: {
    padding: '12px 16px', borderRadius: 10, fontSize: 14,
    textAlign: 'left', display: 'flex', alignItems: 'center',
    gap: 12, border: '1.5px solid #e2e8f0', cursor: 'pointer',
    transition: 'all 0.2s', fontWeight: 500
  },
  optKey: {
    width: 28, height: 28, borderRadius: '50%',
    background: '#fff', display: 'flex', alignItems: 'center',
    justifyContent: 'center', fontSize: 12, fontWeight: 700,
    border: '1.5px solid #667eea', color: '#667eea', flexShrink: 0
  },
  explanation: {
    marginTop: 20, padding: '1rem', background: '#eef2ff',
    borderRadius: 10, fontSize: 14, lineHeight: 1.6,
    borderLeft: '4px solid #667eea'
  },
  nextBtn: {
    marginTop: 20, width: '100%', padding: '13px',
    background: '#667eea', color: '#fff', borderRadius: 10,
    fontSize: 15, fontWeight: 600
  },
  scoreBar: {
    marginTop: 16, textAlign: 'center',
    fontSize: 14, color: '#667eea', fontWeight: 600
  },
  btn: { padding: '10px 24px', background: '#667eea', color: '#fff', borderRadius: 8, fontSize: 14 }
}