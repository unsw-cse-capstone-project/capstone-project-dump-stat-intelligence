// from next-realworld-app
export const paging = (limit, page) =>
  `limit=${limit}&offset=${page ? page * limit : 0}`;
