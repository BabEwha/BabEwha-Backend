import express from 'express';
import 'express-async-errors';
import * as paymentController from '../controller/payment.js';
import { isAuth } from '../middleware/auth.js';

const router = express.Router();

router.post('/', isAuth, speakingController.createPayment);
router.get('/', isAuth, speakingController.getPayment);
router.get('/:id', isAuth, speakingController.getPaymentId);
router.get('/:id', isAuth, speakingController.mofifyPayment);

export default router;
