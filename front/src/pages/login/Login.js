import React from 'react';
import { useForm } from 'react-hook-form';

import styles from './Login.module.scss';
import { login } from '../../api/golem_api';


const Login = () => {
    const {
        register,
        handleSubmit
    } = useForm();

    const mySubmit = async (formData) => {
        const result = await login(formData);
        console.log(result)
    }

    return (
        <div className={styles.container}>
            <form className={styles.loginForm} onSubmit={handleSubmit(mySubmit)}>
                <label className={styles.input_label}>
                    email
                    <input type="email" placeholder="email" className={styles.input} {...register('username', { required: true })} />
                </label>

                <label className={styles.input_label}>
                    pw
                    <input type="password" placeholder="pw" className={styles.input} {...register('password', { required: true })} />
                </label>

                <div className={styles.checkboxContainer}>
                    <label>
                        <input type="checkbox" />
                        email 저장
                    </label>
                    <label>
                        <input type="checkbox" />
                        자동로그인
                    </label>
                </div>
                <button className={styles.loginButton} type="submit">입장하기</button>
                <div className={styles.findPw}>pw 찾기</div>
            </form>
        </div>
    );
};

export default Login;
