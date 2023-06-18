import { urbanist } from './_app'
import Hero from '@/components/hero'
import Navbar from '@/components/navbar'


export default function Home() {
  return (
    <main
      className="
        bg-pale-green 
        min-h-screen 
        font-sans"
    >
      <div className={urbanist.className}>
        <Navbar />
        <Hero />
      </div>
    </main>
  )
}
