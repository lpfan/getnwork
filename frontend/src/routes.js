export const routes = [
  { path: '/categories/', component: CategoryList},
  { path: '/categories/:categories_slug/posts/', component: CategoryPostList },
  { path: '/categories/:categories_slug/posts/:post_slug/', component: PostDetail}
];
