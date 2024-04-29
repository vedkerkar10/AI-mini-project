import { useState } from 'react';

function MyForm() {
    const [ocrResult, setOcrResult] = useState('');
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileUpload = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        const formData = new FormData();
        formData.append('ocrResult', ocrResult);
        formData.append('file', selectedFile);

        try {
            const response = await fetch('http://localhost:5000/submit_form', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            console.log('Response from server:', data);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit} className="mx-auto mb-0 mt-8 max-w-md space-y-4">
                <div>
                    <label htmlFor="uploadInput" className="sr-only">Upload Image</label>
                    <input
                        type="file"
                        id="uploadInput"
                        accept="image/*"
                        onChange={handleFileUpload}
                    />
                </div>
                <div>
                    <label htmlFor="output" className="sr-only">OCR Output</label>
                    <textarea
                        id="output"
                        className="w-full resize-none border-x-0 border-t-0 border-gray-200 px-0 align-top sm:text-sm"
                        rows="4"
                        placeholder="OCR Output..."
                        value={ocrResult}
                        onChange={(e) => setOcrResult(e.target.value)}
                    ></textarea>
                </div>
                <div>
                    <input type="submit" value="Submit" />
                </div>
            </form>
        </div>
    );
}

export default MyForm;
