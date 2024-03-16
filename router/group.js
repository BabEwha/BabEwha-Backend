import express from 'express';
import 'express-async-errors';
import { body } from 'express-validator';
import {validate} from '../middleware/validator.js';
import * as categoryController from '../controller/group.js';
import { isAuth } from '../middleware/auth.js';

const router = express.Router();

router.get('/:id', isAuth, groupController.getGroup);
router.post('/', isAuth, groupController.createGroup);
router.patch('/:id', isAuth, groupController.updateGroup);
router.delete('/:id', isAuth, groupController.deleteGroup);

export default router;
