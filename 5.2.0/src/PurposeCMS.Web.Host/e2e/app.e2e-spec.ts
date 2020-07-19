import { PurposeCMSTemplatePage } from './app.po';

describe('PurposeCMS App', function() {
  let page: PurposeCMSTemplatePage;

  beforeEach(() => {
    page = new PurposeCMSTemplatePage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
