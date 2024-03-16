import jwt from 'jsonwebtoken';
import * as userRepository from '../data/auth.js';
import {config} from '../config.js';

const AUTH_ERROR = {message: 'Authentication Error'};
const EWHAIN_ERROR = {message: '이화인 계정이 아닙니다.'};

export const isAuth = async (req, res, next) => { 
    const authHeader = req.get('Authorization');
    if (!(authHeader && authHeader.startsWith('Bearer '))) { 
        return res.status(401).json(AUTH_ERROR);
    }
    
    const token = authHeader.split(' ')[1];

    jwt.verify(
        token, 
        config.jwt.secretKey,
        async (error, decoded) => {
            if (error) {
                return res.status(401).json({isSuccess: false,
                    code: 401, 
                    message: '인증되지 않은 사용자입니다.'});
            }
            const user = await userRepository.findById(decoded.id);
            if (!user) {
                return res.status(401).json({isSuccess: false,
                    code: 401, 
                    message: '인증되지 않은 사용자입니다.'});
            }
            // 이화인(벗) 인증
            if (!user.email.endsWith('@ewhain.net')) {
                return res.status(401).json(EWHAIN_ERROR);
            }
            req.user_id = user.id;
            req.token = token;
            next();
        }
    );
}
