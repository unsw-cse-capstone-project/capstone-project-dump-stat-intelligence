import Head from "next/head";
import React from "react";

import Preview from "../../components/creator/Preview";

import { useRouter } from "next/router";
import { useEffect } from "react";

import { useSelector, useDispatch } from "react-redux";
import { update_create } from "../../lib/redux/actions/createAction";

export default function Create(props) {
  let isLoggedIn = useSelector((state) => state.auth.isLoggedIn);
  const router = useRouter();
  useEffect(() => {
    if (!isLoggedIn) {
      router.push("/");
    }
  }, []);

  const dispatch = useDispatch();
  let edit = useSelector((state) => state.create);
  function partialUpdate(event, cat) {
    dispatch(update_create(cat, event.target.value));
  }
  return (
    <>
      <Head>
        <title>Pantry Pirate | Create</title>
      </Head>
      <Preview />
    </>
  );
}
