<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SecureShare - Privacy-Preserving Data Platform</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css" rel="stylesheet">
    <script src="https://unpkg.com/crypto-js@4.1.1/crypto-js.js"></script>
</head>
<body class="bg-gray-50">
    <nav class="bg-cyan-600 text-white p-4">
        <div class="container mx-auto flex justify-between items-center">
            <h1 class="text-2xl font-bold">SecureShare</h1>
            <div class="space-x-4">
                <button id="loginBtn" class="px-4 py-2 bg-white text-cyan-600 rounded-lg">Login</button>
                <button id="registerBtn" class="px-4 py-2 border border-white rounded-lg">Register</button>
            </div>
        </div>
    </nav>

    <main class="container mx-auto p-4">
        <!-- File Sharing Section -->
        <div id="shareSection" class="hidden">
            <div class="bg-white p-6 rounded-lg shadow-md mb-6">
                <h2 class="text-2xl font-bold mb-4">Share Sensitive Data</h2>
                <div class="space-y-4">
                    <div>
                        <label class="block mb-2">Select File Type</label>
                        <select id="fileType" class="w-full p-2 border rounded">
                            <option value="medical">Medical Records</option>
                            <option value="financial">Financial Records</option>
                            <option value="personal">Personal Data</option>
                        </select>
                    </div>
                    <div>
                        <label class="block mb-2">Upload File</label>
                        <input type="file" id="fileUpload" class="w-full p-2 border rounded">
                    </div>
                    <div>
                        <label class="block mb-2">Recipient's Email</label>
                        <input type="email" id="recipientEmail" class="w-full p-2 border rounded">
                    </div>
                    <button id="shareBtn" class="bg-cyan-600 text-white px-6 py-2 rounded-lg">
                        Share Securely
                    </button>
                </div>
            </div>

            <!-- Shared Files List -->
            <div class="bg-white p-6 rounded-lg shadow-md">
                <h2 class="text-2xl font-bold mb-4">Shared Files</h2>
                <div id="sharedFilesList" class="space-y-2">
                    <!-- Files will be listed here -->
                </div>
            </div>
        </div>

        <!-- Login Form -->
        <div id="loginForm" class="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md">
            <h2 class="text-2xl font-bold mb-4">Login</h2>
            <div class="space-y-4">
                <div>
                    <label class="block mb-2">Email</label>
                    <input type="email" id="loginEmail" class="w-full p-2 border rounded">
                </div>
                <div>
                    <label class="block mb-2">Password</label>
                    <input type="password" id="loginPassword" class="w-full p-2 border rounded">
                </div>
                <button id="submitLogin" class="w-full bg-cyan-600 text-white px-6 py-2 rounded-lg">
                    Login
                </button>
            </div>
        </div>
    </main>

    <!-- Toast Notification -->
    <div id="toast" class="fixed bottom-4 right-4 bg-green-500 text-white p-4 rounded-lg hidden"></div>

    <script>
        // Simulated user authentication
        let isAuthenticated = false;
        const users = [];

        // UI Elements
        const loginForm = document.getElementById('loginForm');
        const shareSection = document.getElementById('shareSection');
        const loginBtn = document.getElementById('loginBtn');
        const registerBtn = document.getElementById('registerBtn');
        const submitLogin = document.getElementById('submitLogin');
        const shareBtn = document.getElementById('shareBtn');
        const toast = document.getElementById('toast');

        // Simulated file sharing system
        const sharedFiles = [];

        // Show toast message
        function showToast(message, type = 'success') {
            toast.textContent = message;
            toast.className = `fixed bottom-4 right-4 p-4 rounded-lg ${type === 'success' ? 'bg-green-500' : 'bg-red-500'} text-white`;
            toast.classList.remove('hidden');
            setTimeout(() => toast.classList.add('hidden'), 3000);
        }

        // Simple encryption function (for demonstration)
        function encryptData(data) {
            return CryptoJS.AES.encrypt(data, 'secret-key').toString();
        }

        // Handle login
        submitLogin.addEventListener('click', () => {
            const email = document.getElementById('loginEmail').value;
            const password = document.getElementById('loginPassword').value;

            if (email && password) {
                isAuthenticated = true;
                loginForm.classList.add('hidden');
                shareSection.classList.remove('hidden');
                showToast('Successfully logged in!');
            }
        });

        // Handle file sharing
        shareBtn.addEventListener('click', () => {
            const fileInput = document.getElementById('fileUpload');
            const recipientEmail = document.getElementById('recipientEmail').value;
            const fileType = document.getElementById('fileType').value;

            if (fileInput.files.length > 0 && recipientEmail) {
                const file = fileInput.files[0];
                const reader = new FileReader();

                reader.onload = function(e) {
                    const encryptedData = encryptData(e.target.result);
                    sharedFiles.push({
                        name: file.name,
                        type: fileType,
                        recipient: recipientEmail,
                        data: encryptedData
                    });
                    updateSharedFilesList();
                    showToast('File shared successfully!');
                };

                reader.readAsDataURL(file);
            } else {
                showToast('Please select a file and enter recipient email', 'error');
            }
        });

        // Update shared files list
        function updateSharedFilesList() {
            const filesList = document.getElementById('sharedFilesList');
            filesList.innerHTML = sharedFiles.map(file => `
                <div class="p-4 border rounded flex justify-between items-center">
                    <div>
                        <p class="font-semibold">${file.name}</p>
                        <p class="text-sm text-gray-600">Shared with: ${file.recipient}</p>
                    </div>
                    <span class="bg-cyan-100 text-cyan-800 px-2 py-1 rounded">${file.type}</span>
                </div>
            `).join('');
        }

        // Toggle login/register forms
        loginBtn.addEventListener('click', () => {
            loginForm.classList.remove('hidden');
            shareSection.classList.add('hidden');
        });
    </script>
</body>
</html>