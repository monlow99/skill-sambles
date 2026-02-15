#!/bin/bash

echo "🚀 Iniciando LuminaNotes..."

# Navegar a la carpeta de la app
cd notes-app

# Instalar dependencias si no existen node_modules
if [ ! -d "node_modules" ]; then
    echo "📦 Instalando dependencias..."
    npm install
fi

# Arrancar el servidor
echo "🌐 Servidor arrancando en http://localhost:5173"
npm run dev -- --host
