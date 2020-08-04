import Head from "next/head";
import Favourites from "../../components/cookbook/Favourites";
import Owned from "../../components/cookbook/Owned";

import { useSelector } from 'react-redux';
import { useRouter } from 'next/router';
import { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { get_owned } from '../../lib/redux/actions/authAction';

export default function CookBook() {
  const dispatch = useDispatch();
  let isLoggedIn = useSelector(state => state.auth.isLoggedIn)
  const router = useRouter();
  useEffect(() => {
    if (!isLoggedIn) {
      router.push("/pantrypirate")
    } else {
      dispatch(get_owned());
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
      </div>
    </>
  );
}
