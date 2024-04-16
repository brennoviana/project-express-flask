import express  from 'express';
import { userRoutes } from '../modules/users/routes/userRoutes.js'

const app = express();

//Middlewares
app.use(express.json());

//Routes
app.use('/users', userRoutes);

export { app };