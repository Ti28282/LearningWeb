import React from 'react';
import ReactDOM from 'react-dom/client';
import RoutePage from './src/RoutePage';
import { AuthProvider } from './src/Components/AuthContext';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <AuthProvider>
            <RoutePage />
        </AuthProvider>
    </React.StrictMode>
);