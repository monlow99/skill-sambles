import { useState, useEffect } from 'react'
import './index.css'

function App() {
  const [notes, setNotes] = useState(() => {
    const saved = localStorage.getItem('lumina-notes')
    return saved ? JSON.parse(saved) : [
      { id: 1, title: 'Bienvenido ✨', content: 'Este es tu espacio para capturar ideas brillantes.', date: new Date().toLocaleDateString() },
      { id: 2, title: 'Tips', content: 'Usa el botón flotante para añadir nuevas notas.', date: new Date().toLocaleDateString() }
    ]
  })

  const [isModalOpen, setIsModalOpen] = useState(false)
  const [newNote, setNewNote] = useState({ title: '', content: '' })

  useEffect(() => {
    localStorage.setItem('lumina-notes', JSON.stringify(notes))
  }, [notes])

  const addNote = () => {
    if (!newNote.title.trim() && !newNote.content.trim()) return
    const note = {
      ...newNote,
      id: Date.now(),
      date: new Date().toLocaleDateString()
    }
    setNotes([note, ...notes])
    setNewNote({ title: '', content: '' })
    setIsModalOpen(false)
  }

  const deleteNote = (id) => {
    setNotes(notes.filter(note => note.id !== id))
  }

  return (
    <div className="app-container">
      <header>
        <h1>LuminaNotes</h1>
        <div style={{ color: 'var(--text-dim)', fontSize: '0.9rem' }}>
          {notes.length} {notes.length === 1 ? 'nota' : 'notas'}
        </div>
      </header>

      <main className="notes-grid">
        {notes.map(note => (
          <div key={note.id} className="note-card">
            <h3>{note.title || 'Sin título'}</h3>
            <p>{note.content}</p>
            <div className="note-footer">
              <span>{note.date}</span>
              <button className="delete-btn" onClick={() => deleteNote(note.id)}>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M3 6h18M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"></path>
                </svg>
              </button>
            </div>
          </div>
        ))}
      </main>

      <button className="fab" onClick={() => setIsModalOpen(true)}>
        +
      </button>

      {isModalOpen && (
        <div className="modal-overlay" onClick={() => setIsModalOpen(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <h2 style={{ marginBottom: '1.5rem', fontWeight: 600 }}>Nueva Nota</h2>
            <input
              type="text"
              placeholder="Título de la idea..."
              value={newNote.title}
              onChange={e => setNewNote({ ...newNote, title: e.target.value })}
              autoFocus
            />
            <textarea
              rows="5"
              placeholder="Escribe algo brillante..."
              value={newNote.content}
              onChange={e => setNewNote({ ...newNote, content: e.target.value })}
            />
            <button className="save-btn" onClick={addNote}>
              Guardar Nota
            </button>
          </div>
        </div>
      )}
    </div>
  )
}

export default App
