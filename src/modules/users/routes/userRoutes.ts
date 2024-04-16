import { Router } from 'express';
import { userController } from '../controller/userController.js';

const userRoutes = Router();

userRoutes.get('/:id', userController.getUserById);

userRoutes.get('/', userController.getAll);

userRoutes.post('/', userController.post);

export { userRoutes };
