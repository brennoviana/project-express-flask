import { Request, Response } from 'express';
import { userRepository } from "../repository/userRepository.js";
import mongoose from 'mongoose';

class UserController {
    async getAll(req: Request, res: Response) {
        try {
        const users = await userRepository.findAll();
    
        if(users.length == 0){
            return res.status(404).send({ message: 'Nenhum usuário cadastrado'})
        };
    
        res.status(200).send(users);
        } catch (error) {
        console.error(error);
        res.status(500).send({ message: 'Erro interno do servidor'});
        }
    };

    async getUserById(req: Request, res: Response): Promise<Response | void> {
        try {
            const userId = req.params.id;

            if (!mongoose.Types.ObjectId.isValid(userId)) {
                return res.status(400).send({ message: 'Formato de ID inválido' });
            }

            const user = await userRepository.find(userId);

            if (!user) {
                return res.status(404).send({ message: 'Usuário não encontrado' });
            }

            res.status(200).send(user);
        } catch (error) {
            console.error(error);
            res.status(500).send({ message: 'Erro interno do servidor' });
        }
    }

    async post(req: Request, res: Response): Promise<void> {
        try {
            const newUser = await userRepository.add(req.body);
            res.status(201).send(newUser);
        } catch (error) {
            console.error(error);
            res.status(400).send({ Error: "Erro ao criar o usuário, verifique os dados fornecidos." });
        }
    }
}

export const userController = new UserController();
