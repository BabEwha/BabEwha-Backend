import express from 'express';
import 'express-async-errors';
import * as speakingController from '../controller/receipt.js';
import { isAuth } from '../middleware/auth.js';

const router = express.Router();

router.post('/', isAuth, speakingController.createReceipt);
router.patch('/', isAuth, speakingController.updateReceipt);
router.get('/:id', isAuth, speakingController.getReceipt);

export default router;
