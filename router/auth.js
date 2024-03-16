import express from 'express';
import 'express-async-errors';
import { body } from 'express-validator';
import {validate} from '../middleware/validator.js';
import * as authController from '../controller/auth.js';
import { isAuth } from '../middleware/auth.js';

const router = express.Router();

const validateCredential = [
    body('email')
        .isEmail()
        .normalizeEmail()
        .withMessage('올바른 이메일 형식이 아닙니다.'),
    body('password')
        .trim()
        .isLength({min:10})
        .withMessage('비밀번호는 10자 이상부터 사용 가능합니다.'),
    validate
];

const validateSignup = [
    ...validateCredential,
    body('nickname')
        .trim()
        .notEmpty()
        .withMessage('닉네임을 한 글자 이상 입력해주세요.'),
    body('phone')
        .trim()
        .isLength({max:15})
        .withMessage('전화번호를 다시 입력해주세요.'), 
    body('bank_name')
        .trim()
        .notEmpty()
        .withMessage('은행 이름을 입력해주세요')
    body('account_number')
        .trim()
        .notEmpty()
        .withMessage('계좌를 입력해주세요')
    body('url')
        .isURL()
        .withMessage('invalid URL')
        .optional({nullable:true, checkFalsy:true}),
        validate
];

router.post('/signup', validateSignup, authController.signup);
router.post('/login', validateCredential, authController.login);
router.get('/me', isAuth, authController.me);
router.delete('/signout', isAuth, 
    [
        body('password')
        .trim()
        .isLength({min:10})
        .withMessage('비밀번호는 10자 이상부터 사용 가능합니다.'),
        validate
    ]
, authController.signout);

export default router;
