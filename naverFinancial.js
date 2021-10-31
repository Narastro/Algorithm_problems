const MAX_PER_PAGE = 10;
const CUR_PAGE_DEFAULT = 1;
const TOTAL_ITEM_DEFAULT = 0;
const PAGE_ITEM_DEFAULLT = 20;

export default class Pagination {
  #currentPage = CUR_PAGE_DEFAULT;
  #totalItemCount = TOTAL_ITEM_DEFAULT;
  #pagePerItemCount = PAGE_ITEM_DEFAULLT;
  #totalPage;
  constructor(param) {
    if (!param) return;
    this.#currentPage = param.currentPage ?? CUR_PAGE_DEFAULT;
    this.#totalItemCount = param.totalItemCount ?? TOTAL_ITEM_DEFAULT;
    this.#pagePerItemCount = param.pagePerItemCount ?? PAGE_ITEM_DEFAULLT;
    this.checkRestrictions();
  }

  setState(nextStateParam) {
    this.#currentPage = nextStateParam.currentPage ?? this.#currentPage;
    this.#totalItemCount =
      nextStateParam.totalItemCount ?? this.#totalItemCount;
    this.#pagePerItemCount =
      nextStateParam.pagePerItemCount ?? this.#pagePerItemCount;
    this.checkRestrictions();
  }

  render() {
    let template = "<div>";
    if (this.#totalItemCount === 0) return `<div></div>`;
    if (this.#currentPage > 1) template += `<span class="prev-page"></span>`;

    const { start, end } = this.calculatePageRange();
    for (let i = start; i < end; i++) {
      if (i === this.#currentPage) {
        template += `<span class="current-page">${i}</span>`;
      } else {
        template += `<span>${i}</span>`;
      }
    }

    if (this.#currentPage !== this.#totalPage)
      template += `<span class="next-page"></span>`;
    template += "</div>";
    return template;
  }

  checkRestrictions() {
    this.checkParameterIsNumber();
    this.checkParameterIsNegativeOrZero();
    this.calculateTotalPage();
    this.checkCurrentPageIsOverflow();
  }

  checkParameterIsNumber() {
    if (typeof this.#currentPage !== "number")
      this.#currentPage = CUR_PAGE_DEFAULT;
    if (typeof this.#totalItemCount !== "number")
      this.#totalItemCount = TOTAL_ITEM_DEFAULT;
    if (typeof this.#pagePerItemCount !== "number")
      this.#pagePerItemCount = PAGE_ITEM_DEFAULLT;
  }

  checkParameterIsNegativeOrZero() {
    if (this.#currentPage <= 0) this.#currentPage = CUR_PAGE_DEFAULT;
    if (this.#totalItemCount < 0) this.#totalItemCount = TOTAL_ITEM_DEFAULT;
    if (this.#pagePerItemCount <= 0)
      this.#pagePerItemCount = PAGE_ITEM_DEFAULLT;
  }

  calculateTotalPage() {
    this.#totalPage = Math.ceil(this.#totalItemCount / this.#pagePerItemCount);
  }

  checkCurrentPageIsOverflow() {
    if (this.#currentPage > this.#totalPage)
      this.#currentPage = this.#totalPage;
  }

  calculatePageRange() {
    const start =
      Math.floor((this.#currentPage - 1) / MAX_PER_PAGE) * MAX_PER_PAGE + 1;
    const end =
      this.#totalPage < start + MAX_PER_PAGE
        ? this.#totalPage + 1
        : start + MAX_PER_PAGE;
    return { start, end };
  }
}

console.log(
  new Pagination({
    currentPage: 17,
    totalItemCount: 4753,
  }).render()
);
