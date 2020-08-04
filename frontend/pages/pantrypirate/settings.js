import Head from "next/head";
import Details from "../../components/settings/Details"
import Password from "../../components/settings/Password"

import { useSelector } from 'react-redux';
import { useRouter } from 'next/router';
import { useEffect } from 'react';




export default function Home() {
  let isLoggedIn = useSelector(state => state.auth.isLoggedIn)
  const router = useRouter();
  useEffect(() => {
    if (!isLoggedIn) {
      router.push("/pantrypirate")
    }
  }, [])
  
  
  return (
    <div>
      <Head>
        <title>Pantry Pirate | Settings</title>
      </Head>
      <div className="container">
        <div className="columns is-centered">
          <div className="box column is-10">
            <h1 className="title is-1">Settings</h1>
            <Details/>
            <Password/>
          </div>
        </div>
      </div>
    </div>
  );
}
