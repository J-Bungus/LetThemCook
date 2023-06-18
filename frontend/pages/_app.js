import '@/styles/globals.css'
import { ChakraProvider } from '@chakra-ui/react'
import { extendTheme } from '@chakra-ui/react';
import { Urbanist } from 'next/font/google';

export const urbanist = Urbanist({ 
  subsets: ['latin'], 
});



function MyApp({ Component, pageProps }) {
  return (
    <ChakraProvider 
      className={urbanist.className} 
    >
      <Component {...pageProps} />
    </ChakraProvider>
  )
}

export default MyApp;