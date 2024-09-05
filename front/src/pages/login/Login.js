// import React from 'react';
// import axios from 'axios';
// import { useForm } from 'react-hook-form';

// import styles from './Login.module.scss';



// const Login = () => {
//     const {
//         register,
//         handleSubmit,
//         formState: { errors },
//     } = useForm({
//         mode: 'onSubmit',
//     });

//     const onSubmit = async (data) => {
//         try {
//             const res = await axios.post('/api/member/login', data);
//             if (res.data.result === 'noSuchId') {
//                 alert('존재하지 않는 아이디입니다.');
//             } else if (res.data.result === 'wrongPw') {
//                 alert('비밀번호가 틀렸습니다.');
//             } else {
//                 alert('로그인 성공');
//                 // 로그인 성공 시 추가 작업이 필요하면 여기에 추가
//             }
//         } catch (e) {
//             alert('오류가 발생했습니다.');
//             console.log(e);
//         }
//     };

//     return (
//         <div className={styles.container}>
//             <form className={styles.loginForm} onSubmit={handleSubmit(onSubmit)}>
//                 <label className={styles.input_label}>
//                     email
//                     <input type="email" placeholder="email" className={styles.input} {...register('id', { required: true })} />
//                 </label>

//                 <label className={styles.input_label}>
//                     pw
//                     <input type="password" placeholder="pw" className={styles.input} {...register('pw', { required: true })} />
//                 </label>

//                 <div className={styles.checkboxContainer}>
//                     <label>
//                         <input type="checkbox" />
//                         email 저장
//                     </label>
//                     <label>
//                         <input type="checkbox" />
//                         자동로그인
//                     </label>
//                 </div>
//                 <button className={styles.loginButton} type="submit">입장하기</button>
//                 <div className={styles.findPw}>pw 찾기</div>
//             </form>
//         </div>
//     );
// };

// export default Login;
