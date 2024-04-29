"use client"
import React, { useState } from 'react';

const Form = () => {
    const [ocrResult, setOcrResult] = useState('');

    const [prompt, setPrompt] = useState('');



    const handleFileUpload = async (event) => {
        const file = event.target.files[0];
        const formData = new FormData();
        formData.append('file', file);
        formData.append('q', prompt);

        try {
            const response = await fetch('http://127.0.0.1:5000/api/ocr', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            console.log(data)
            setOcrResult(data.text);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div>
            <form action="#" className="mx-auto mb-0 mt-8 max-w-md space-y-4">
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
                        className="w-full resize-none border-x-0 border-t-0 border-gray-200 px-0 align-top sm:text-sm text-black"
                        rows="4"
                        placeholder="OCR Output..."
                        value={prompt}
                        onChange={(e) => {
                            setPrompt(e.target.value)
                        }}
                    ></textarea>
                </div>
                <div>
                    <input type="submit" />
                </div>
                {ocrResult}
            </form>
        </div>
    );
}

export default Form;
