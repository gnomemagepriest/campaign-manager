import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import "../styles/Form.css";

function Register() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [passwordRepeated, setPasswordRepeated] = useState("");
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const res = await api.post("/api/user/register/", {
                username,
                password,
            });
            navigate("/login");
        } catch (error) {
            console.log(error);
        }
    };

    const buttonDisabled = () => {
        if (username === "") {
            return true;
        }

        if (password === "") {
            return true;
        }

        return password !== passwordRepeated;
    }

    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h1>Регистрация</h1>
            <input
                className="form-input"
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Введите логин"
            />
            <input
                className="form-input"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Введите пароль"
            />
            <input
                className="form-input"
                type="password"
                value={passwordRepeated}
                onChange={(e) => setPasswordRepeated(e.target.value)}
                placeholder="Введите пароль повторно"
            />
            <button
                className="form-button"
                type="submit"
                disabled={buttonDisabled()}
            >
                Зарегистрироваться
            </button>
        </form>
    );
}

export default Register;
