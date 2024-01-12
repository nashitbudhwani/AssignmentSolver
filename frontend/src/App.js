import { React } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SubmitAssignment from './pages/submitAssignment.js';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<SubmitAssignment />}></Route>
      </Routes>
    </Router>
    );
}

export default App;
