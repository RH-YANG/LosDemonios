import React from 'react';
import styles from './Navi.module.scss';
import naviImage from '../../assets/image/navi_basic_upload.png';

const Navi = ({ message }) => {
    return (
        <div className={styles.navi_div}>
            <img src={naviImage} alt="Basic Navi" className={styles.image} />
            <div className={styles.message}>
                {message.split('\n').map((line, index) => (
                    <span key={index}>
                        {line}
                        <br />
                    </span>
                ))}
            </div>
        </div>
    );
};

export default Navi;