import { app } from "./app/app.js"
import { config } from './config/envConfig.js';
import { connectToDatabase } from './config/dbConfig.js'

connectToDatabase();

const PORT = config.port;

app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
})