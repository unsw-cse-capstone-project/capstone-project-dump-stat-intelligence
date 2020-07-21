import Head from "next/head";
import Favourites from "../components/cookbook/Favourites";
import Owned from "../components/cookbook/Owned";
import Suggset from "../components/cookbook/Suggest";

import { useSelector } from 'react-redux';
import { useRouter } from 'next/router';
import { useEffect } from 'react';

export default function CookBook() {
  let isLoggedIn = useSelector(state => state.auth.isLoggedIn)
  const router = useRouter();
  useEffect(() => {
    if (!isLoggedIn) {
      router.push("/")
    }
  }, [])
  return (
    <>
      <Head>
        <title>Pantry Pirate | Cookbook</title>
      </Head>
      <div>
        <Favourites/>
        <hr/>
        <Owned/>
        <hr/>
        <Suggset/>
      </div>
    </>
  );
}
