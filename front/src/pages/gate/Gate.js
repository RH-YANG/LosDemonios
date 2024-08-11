import React from 'react';
import { useNavigate } from 'react-router-dom';

import styles from './Gate.module.scss';
import Navi from '../../component/navi/Navi';



const Gate = () => {
    const message = `
        안녕?
        난 로디를 이끌어가는 신, 네비게이터야
        로디에 접속하기 위해서는 너의 분신이 필요해
        계정이 있니?
    `;

    const navigate = useNavigate();

    const handleYesClick = () => {
        navigate('/login');
    };

    const handleNoClick = () => {
        navigate('/join')
    };

    return (
        <div className={styles.container}>
            <Navi message={message} />
            <div className={styles.button_div}>
                <button className={styles.button} onClick={handleYesClick}>
                    응
                </button>
                <button className={styles.button} onClick={handleNoClick}>
                    아니
                </button>
            </div>

        </div>
    );
};

export default Gate;