import express from 'express';
import 'express-async-errors';
import { body } from 'express-validator';
import {validate} from '../middleware/validator.js';
import * as categoryController from '../controller/group.js';
import { isAuth } from '../middleware/auth.js';

const router = express.Router();

router.post('/', isAuth, categoryController.createGroup);
router.put('/:id', isAuth, categoryController.updateGroup);
router.delete('/:id', isAuth, categoryController.deleteGroup);

export default router;
