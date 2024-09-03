import React, { useState } from 'react';
import './App.css';

function App() {
  const [form, setForm] = useState({
    name: '',
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({
      ...form,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log('Form submitted:', form);

    // 서버로 폼 데이터를 전송하는 로직
    try {
      const response = await fetch('https://0.0.0.0:11888/join', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log('Success:', data);
      // TODO: 서버 응답에 따라 추가 로직을 실행 (예: 사용자에게 성공 메시지 표시)
    } catch (error) {
      console.error('Error:', error);
      // TODO: 에러 처리 로직 추가 (예: 사용자에게 에러 메시지 표시)
    }
  };

  return (
    <div className="App">
      <h2>회원가입</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">이름 : </label>
          <input
            type="text"
            id="name"
            name="name"
            value={form.name}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="email">이메일 : </label>
          <input
            type="email"
            id="email"
            name="email"
            value={form.email}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="password">비밀번호 : </label>
          <input
            type="password"
            id="password"
            name="password"
            value={form.password}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">가입하기</button>
      </form>
    </div>
  );
}

export default App;