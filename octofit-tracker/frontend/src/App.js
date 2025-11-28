import logo from './octofitapp-small.png';


function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div className="container-fluid d-flex align-items-center">
          <img src={logo} alt="OctoFit Logo" className="octofit-logo" />
          <Link className="navbar-brand fw-bold d-flex align-items-center" to="/">OctoFit Tracker</Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container">
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={
            <div className="card text-center mt-5">
              <div className="card-body">
                <h1 className="card-title display-4 mb-3">Welcome to <span className="text-primary">OctoFit Tracker</span>!</h1>
                <p className="card-text lead">Track your fitness, join teams, and compete on the leaderboard.</p>
                <Link to="/activities" className="btn btn-lg btn-primary mt-3">Get Started</Link>
              </div>
            </div>
          } />
        </Routes>
      </div>
    </div>
  );
}

export default App;
