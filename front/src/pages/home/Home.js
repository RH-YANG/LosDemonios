import React from 'react';
import { useNavigate } from 'react-router-dom';

import styles from './Home.module.scss';
import logo from '../../assets/image/logo.png';



const Home = () => {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/about');
    };


    return (
        <div className={styles.container}>
            <div className={styles.content}>
                <img src={logo} alt="los Demonios" className={styles.logo} />
                <p className={styles.quote}>"빛에는 반드시 그림자가 뒤따르는 법"</p>
                <p className={styles.text}>
                    19세기 말, 미국 서부에 새로운 도시가 세워졌다.
                    <br />
                    태양 아래 빛나는 야자수와 무한한 축복의 땅,
                    <br />
                    로스 앤젤레스.
                    <br />
                    <br />
                    그러나 이 도시가 건설될 때,
                    <br />
                    그 이면에는 아무도 알지 못하는 또 다른 세계가 생겨나고 있었다.
                    <br />
                    그곳은 악령들의 땅,
                    <br />
                    '로스 디모니오스'라 불렸다.
                </p>
                <div onClick={handleClick} className={styles.arrow}>»»»</div>
            </div>
        </div>
    );
};

export default Home;
