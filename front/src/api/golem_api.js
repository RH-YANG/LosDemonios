import axios from 'axios'; // index.js에 기본값 지정해놓음



export const login = async (req) =>{
    try {
        // OAuth2 규격을 위한 설정
        const config = {headers: {'Content-Type': 'application/x-www-form-urlencoded'}};
        const params = new URLSearchParams();
        params.append('username', req.username);
        params.append('password', req.password);

        const res = await axios.post('golem/login', params, config).then(res=>res.data);
        return res;

    } catch (e) {
        alert('서버측에서 오류가 발생했습니다');
        console.log(e);
    }
}