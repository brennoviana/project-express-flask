import express  from 'express';
import { userRoutes } from '../modules/users/routes/userRoutes.js'
import path from 'path';
import { fileURLToPath } from 'url';

const app = express();
const __dirname = path.dirname(fileURLToPath(import.meta.url));

//Middlewares
app.use(express.json());
app.use(express.static(path.join(__dirname, '../../public')));

//Routes
app.use('/users', userRoutes);

export { app };