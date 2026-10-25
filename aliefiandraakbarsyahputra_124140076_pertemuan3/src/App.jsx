import { Link, NavLink, Route, Routes } from 'react-router-dom';
import Home from './pages/Home/Home.jsx';
import Stats from './pages/Stats/Stats.jsx';

// Komponen root: navigasi multi-halaman dengan React Router
export default function App() {
  return (
    <>
      <header className="topbar">
        <h1>Rak Buku</h1>
        <nav aria-label="Navigasi utama">
          <NavLink to="/" end>Koleksi</NavLink>
          <NavLink to="/stats">Statistik</NavLink>
        </nav>
      </header>
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/stats" element={<Stats />} />
          <Route path="*" element={<p>Halaman tidak ditemukan. <Link to="/">Kembali ke koleksi</Link></p>} />
        </Routes>
      </main>
    </>
  );
}
