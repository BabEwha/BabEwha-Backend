import express from 'express';
import 'express-async-errors';
import * as paymentController from '../controller/payment.js';
import { isAuth } from '../middleware/auth.js';

const router = express.Router();

router.post('/', isAuth, paymentController.createPayment);
router.get('/', isAuth, paymentController.getPayment);
router.get('/:id', isAuth, paymentController.getPaymentId);
router.patch('/:id', isAuth, paymentController.updatePayment);

export default router;
