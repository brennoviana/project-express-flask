// Importando dependências necessárias
import { userModel } from "../model/userModel.js";
import { IUser } from "../model/userModel"; 

class UserRepository {
    async find(id: string): Promise<IUser | null> {
        return userModel.findById(id);
    }

    async findAll(): Promise<IUser[] | null> {
        return userModel.find().exec();
    }

    async add(userData: IUser): Promise<IUser> {
        const newUser = new userModel(userData);
        return newUser.save();
    }
}

export const userRepository = new UserRepository();
