// pages/index.js
import React from 'react';
import Header from './_components/Header';

export default function Home() {
  return (
    <div>
      <Header />
      <div className='flex m-3'>
        <label htmlFor="uploadInput">Input Image:  </label>
        <input
          type="file"
          id="uploadInput"
          accept="image/*"
        />
      </div>
    </div>
  );
}
