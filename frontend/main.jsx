import React from 'react';
import ReactDOM from 'react-dom/client';
// import Loading from './src/components/loading/loading';
import RoutePage from './src/routePage';
import { AuthProvider } from './src/Components/authContext';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <AuthProvider>
            <RoutePage />
        </AuthProvider>
    </React.StrictMode>
);